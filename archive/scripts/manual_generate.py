
import argparse
import os
import sys
import time
import json
import io
import google.generativeai as genai
from PIL import Image

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
            elif line.startswith('Prompt:') or line.startswith('Panel') or line.startswith('Style:'):
                prompt_lines.append(line)
    
    # Save last entry
    if current_entry and 'id' in current_entry:
        full_prompt = '\n'.join(prompt_lines).strip()
        current_entry['full_prompt'] = full_prompt
        entries.append(current_entry)
    
    return entries

def generate_image_gemini(model, prompt):
    """Generate image using Gemini native image generation."""
    try:
        response = model.generate_content(
            prompt,
            generation_config=genai.types.GenerationConfig(
                response_mime_type="image/jpeg"
            )
        )
        if response.parts:
            return response.parts[0].inline_data.data
    except Exception as e:
        print(f"Error generating image: {e}")
    return None

def main():
    parser = argparse.ArgumentParser(description='Batch Image Generation')
    parser.add_argument('--api_key', required=True, help='Gemini API Key')
    parser.add_argument('--input_file', required=True, help='Path to prompt file')
    parser.add_argument('--output_dir', required=True, help='Output directory')
    args = parser.parse_args()

    genai.configure(api_key=args.api_key)
    # Using the model that corresponds to "Nano Banana" (Gemini 3 Pro equivalent if available, or latest stable)
    # Since specific model names change, we'll try a standard one or the one from the original script
    model = genai.GenerativeModel('gemini-1.5-pro-latest') # Fallback to 1.5 Pro if 3 is not public yet via this lib

    os.makedirs(args.output_dir, exist_ok=True)
    entries = parse_prompt_file(args.input_file)

    print(f"Found {len(entries)} items to process.")

    for entry in entries:
        image_id = entry['id']
        word = entry['word']
        filename = f"{image_id}_{word}.jpg"
        filepath = os.path.join(args.output_dir, filename)

        if os.path.exists(filepath):
            print(f"Skipping {filename} (already exists)")
            continue

        print(f"Generating {filename}...")
        image_data = generate_image_gemini(model, entry['full_prompt'])

        if image_data:
            with open(filepath, 'wb') as f:
                f.write(image_data)
            print(f"Saved {filename}")
        else:
            print(f"Failed to generate {filename}")
        
        time.sleep(2) # Rate limiting

if __name__ == "__main__":
    main()
