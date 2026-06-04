"""
Gemini API / Imagen API image batch generation for Italian vocab cards.

Usage:
  pip install google-genai Pillow
  set GEMINI_API_KEY=your_api_key_here

  # Gemini native image gen (default)
  python generate_images_gemini.py --prompt-file ../genspark_prompts_batch3.txt --output-dir ../assets/images/batch3

  # Imagen model (separate quota!)
  python generate_images_gemini.py --prompt-file ../genspark_prompts_batch3.txt --output-dir ../assets/images/batch3 --use-imagen

  # Auto-fallback: try Imagen first, fallback to Gemini if quota exhausted
  python generate_images_gemini.py --prompt-file ../genspark_prompts_batch3.txt --output-dir ../assets/images/batch3 --use-imagen --fallback
"""

import argparse
import os
import sys
import time
import json
import io
from datetime import datetime


def parse_prompt_file(filepath):
    """Parse prompt text file and return list of image entries."""
    entries = []
    current_entry = {}
    prompt_lines = []
    
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.rstrip('\r\n')
            
            if line.startswith('---'):
                if current_entry and 'id' in current_entry:
                    full_prompt = '\n'.join(prompt_lines).strip()
                    current_entry['full_prompt'] = full_prompt
                    entries.append(current_entry)
                current_entry = {}
                prompt_lines = []
                continue
            
            if line.startswith('Image ID:'):
                current_entry['id'] = int(line.split(':')[1].strip())
            elif line.startswith('Word:'):
                current_entry['word'] = line.split(':', 1)[1].strip()
            elif line.startswith('Story:'):
                current_entry['story'] = line.split(':', 1)[1].strip()
            elif line.startswith('Prompt:') or line.startswith('Panel') or line.startswith('Style:'):
                prompt_lines.append(line)
    
    # Save last entry
    if current_entry and 'id' in current_entry:
        full_prompt = '\n'.join(prompt_lines).strip()
        current_entry['full_prompt'] = full_prompt
        entries.append(current_entry)
    
    return entries


def generate_image_gemini(client, model, prompt):
    """Generate image using Gemini native image generation (generate_content)."""
    from google.genai import types
    
    response = client.models.generate_content(
        model=model,
        contents=[prompt],
        config=types.GenerateContentConfig(
            response_modalities=['TEXT', 'IMAGE'],
        ),
    )
    
    if response.candidates and response.candidates[0].content:
        for part in response.candidates[0].content.parts:
            if part.inline_data is not None:
                return part.inline_data.data, part.inline_data.mime_type
    
    return None, None


def generate_image_imagen(client, model, prompt):
    """Generate image using Imagen model (generate_images)."""
    from google.genai import types
    
    response = client.models.generate_images(
        model=model,
        prompt=prompt,
        config=types.GenerateImagesConfig(
            number_of_images=1,
        ),
    )
    
    if response.generated_images and len(response.generated_images) > 0:
        img = response.generated_images[0].image
        # img is a PIL-like object with .image_bytes or we can save it
        buf = io.BytesIO()
        img.save(buf, format='PNG')
        return buf.getvalue(), 'image/png'
    
    return None, None


def generate_with_retry(client, prompt, use_imagen, fallback, retry_count=3, delay=5):
    """Generate image with retry logic and optional fallback between models."""
    
    GEMINI_MODEL = 'gemini-2.5-flash-image'
    IMAGEN_MODEL = 'imagen-3.0-generate-002'
    
    # Determine model order
    if use_imagen:
        models = [(IMAGEN_MODEL, generate_image_imagen)]
        if fallback:
            models.append((GEMINI_MODEL, generate_image_gemini))
    else:
        models = [(GEMINI_MODEL, generate_image_gemini)]
        if fallback:
            models.append((IMAGEN_MODEL, generate_image_imagen))
    
    for model_name, gen_func in models:
        for attempt in range(retry_count):
            try:
                image_data, mime_type = gen_func(client, model_name, prompt)
                
                if image_data:
                    return image_data, mime_type, model_name
                
                print(f"    [!] No image returned from {model_name}")
                if attempt < retry_count - 1:
                    wait = delay * (attempt + 1)
                    print(f"    ... retry in {wait}s ({attempt + 2}/{retry_count})")
                    time.sleep(wait)
                    
            except Exception as e:
                error_msg = str(e)
                is_quota = '429' in error_msg or 'quota' in error_msg.lower() or 'RESOURCE_EXHAUSTED' in error_msg
                
                if is_quota:
                    print(f"    [QUOTA] {model_name} quota exhausted!")
                    if fallback and len(models) > 1:
                        print(f"    -> Switching to fallback model...")
                        break  # Break retry loop, try next model
                    else:
                        wait = 60 * (attempt + 1)
                        print(f"    ... waiting {wait}s before retry...")
                        time.sleep(wait)
                else:
                    print(f"    [ERR] {error_msg[:150]}")
                    if attempt < retry_count - 1:
                        wait = delay * (attempt + 1)
                        print(f"    ... retry in {wait}s ({attempt + 2}/{retry_count})")
                        time.sleep(wait)
        else:
            # All retries exhausted for this model, continue to fallback if available
            continue
    
    return None, None, None


def get_extension(mime_type):
    """Get file extension from MIME type."""
    mapping = {
        'image/png': '.png',
        'image/jpeg': '.jpg',
        'image/webp': '.webp',
    }
    return mapping.get(mime_type, '.png')


def load_progress(progress_file):
    """Load progress from file."""
    if os.path.exists(progress_file):
        with open(progress_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {"completed": [], "failed": [], "last_updated": None}


def save_progress(progress_file, progress):
    """Save progress to file."""
    progress["last_updated"] = datetime.now().isoformat()
    with open(progress_file, 'w', encoding='utf-8') as f:
        json.dump(progress, f, indent=2, ensure_ascii=False)


def main():
    parser = argparse.ArgumentParser(description='Gemini/Imagen API image batch generation')
    parser.add_argument('--prompt-file', required=True, help='Prompt file path')
    parser.add_argument('--output-dir', required=True, help='Output directory')
    parser.add_argument('--start-id', type=int, default=None, help='Start Image ID')
    parser.add_argument('--end-id', type=int, default=None, help='End Image ID')
    parser.add_argument('--delay', type=float, default=5, help='Delay between requests (seconds)')
    parser.add_argument('--retry', type=int, default=3, help='Retry count on failure')
    parser.add_argument('--api-key', default=None, help='Gemini API key')
    parser.add_argument('--use-imagen', action='store_true', help='Use Imagen model (separate quota)')
    parser.add_argument('--fallback', action='store_true', help='Fallback to other model if quota exhausted')
    args = parser.parse_args()
    
    # Check API key
    api_key = args.api_key or os.environ.get('GEMINI_API_KEY') or os.environ.get('GOOGLE_API_KEY')
    if not api_key:
        print("[ERROR] API key required!")
        print("  Option 1: set GEMINI_API_KEY=your_key")
        print("  Option 2: --api-key your_key")
        print("  Get key at: https://aistudio.google.com/apikey")
        sys.exit(1)
    
    # Initialize client
    try:
        from google import genai
        client = genai.Client(api_key=api_key)
    except ImportError:
        print("[ERROR] Install required: pip install google-genai Pillow")
        sys.exit(1)
    
    model_label = "imagen-3.0-generate-002" if args.use_imagen else "gemini-2.5-flash-image"
    fallback_label = " (+fallback)" if args.fallback else ""
    print(f"[OK] Client initialized. Model: {model_label}{fallback_label}")
    
    # Parse prompt file
    print(f"[..] Parsing: {args.prompt_file}")
    entries = parse_prompt_file(args.prompt_file)
    print(f"     Found {len(entries)} entries")
    
    if not entries:
        print("[ERROR] No prompts found.")
        sys.exit(1)
    
    # Filter by ID range
    if args.start_id is not None:
        entries = [e for e in entries if e['id'] >= args.start_id]
    if args.end_id is not None:
        entries = [e for e in entries if e['id'] <= args.end_id]
    
    print(f"     Processing: {len(entries)} entries (ID {entries[0]['id']} ~ {entries[-1]['id']})")
    
    # Create output directory
    os.makedirs(args.output_dir, exist_ok=True)
    
    # Load progress
    progress_file = os.path.join(args.output_dir, '_progress.json')
    progress = load_progress(progress_file)
    
    completed_ids = set(progress["completed"])
    remaining = [e for e in entries if e['id'] not in completed_ids]
    
    if completed_ids:
        print(f"     Already done: {len(completed_ids)}, remaining: {len(remaining)}")
    
    if not remaining:
        print("[DONE] All images already generated!")
        return
    
    # Start generation
    print(f"\n{'='*60}")
    print(f"[START] Generating {len(remaining)} images")
    print(f"  Model: {model_label}{fallback_label}")
    print(f"  Delay: {args.delay}s | Retry: {args.retry}x")
    print(f"{'='*60}\n")
    
    success_count = 0
    fail_count = 0
    start_time = time.time()
    
    for idx, entry in enumerate(remaining):
        image_id = entry['id']
        word = entry['word']
        
        print(f"[{idx+1}/{len(remaining)}] ID {image_id}: {word}")
        
        image_data, mime_type, used_model = generate_with_retry(
            client, entry['full_prompt'],
            use_imagen=args.use_imagen, fallback=args.fallback,
            retry_count=args.retry, delay=args.delay
        )
        
        if image_data:
            ext = get_extension(mime_type)
            filename = f"{image_id}_{word}{ext}"
            filepath = os.path.join(args.output_dir, filename)
            
            with open(filepath, 'wb') as f:
                f.write(image_data)
            
            model_tag = f" ({used_model.split('-')[0]})" if used_model else ""
            print(f"    [OK] Saved: {filename}{model_tag}")
            success_count += 1
            progress["completed"].append(image_id)
        else:
            print(f"    [FAIL] ID {image_id} ({word})")
            fail_count += 1
            progress["failed"].append({"id": image_id, "word": word})
        
        save_progress(progress_file, progress)
        
        if idx < len(remaining) - 1:
            time.sleep(args.delay)
    
    # Summary
    elapsed = time.time() - start_time
    print(f"\n{'='*60}")
    print(f"[DONE]")
    print(f"  Time: {elapsed/60:.1f} min")
    print(f"  Success: {success_count}")
    print(f"  Failed: {fail_count}")
    print(f"  Output: {os.path.abspath(args.output_dir)}")
    
    if progress["failed"]:
        print(f"\n  Failed items:")
        for item in progress["failed"]:
            print(f"    - ID {item['id']}: {item['word']}")
        print(f"\n  Re-run same command to retry failed items (completed ones are skipped)")
    
    print(f"{'='*60}")


if __name__ == '__main__':
    main()
