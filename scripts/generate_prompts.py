import json
import os

def generate_prompts(json_path, output_path):
    print(f"Reading JSON from: {json_path}")
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            vocab_list = json.load(f)
    except FileNotFoundError:
        print(f"Error: File not found at {json_path}")
        return

    # Helper to find item by word (simplified for this script)
    def find_item(target_word):
        for item in vocab_list:
            if item['word'].lower() == target_word.lower():
                return item
        return None

def generate_prompts(json_path, output_path, limit=None):
    print(f"Reading JSON from: {json_path}")
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except Exception as e:
        print(f"Error reading JSON: {e}")
        return

    prompts = []
    processed_count = 0
    
    for item in data:
        # Only process words that have an enriched story
        story_raw = item.get('story', '')
        if not story_raw or story_raw == "":
            continue
            
        # Determine Gender Label
        gender_raw = item.get('gender', '').lower()
        gender_label = ""
        if 's.m.' in gender_raw:
            gender_label = "(m)"
        elif 's.f.' in gender_raw:
            gender_label = "(f)"
        
        # Text to display on image
        display_text = f"{item['word']} {gender_label}".strip()

        # Split story into panels
        panels = story_raw.split('. ')
        if len(panels) < 4:
            # Fallback for short stories
            panel_texts = [story_raw] * 4
        else:
            panel_texts = panels[:4]

        # 4-Panel Story Comic Prompt - V7
        prompt = (
            f"Image ID: {item['id']}\n"
            f"Word: {item['word']}\n"
            f"Story: {story_raw}\n"
            f"Prompt: A 4-panel grid comic strip telling a story for the word '{item['word']}'.\n"
            f"Panel 1: {panel_texts[0]}\n"
            f"Panel 2: {panel_texts[1]}\n"
            f"Panel 3: {panel_texts[2]}\n"
            f"Panel 4: {panel_texts[3]}\n"
            f"Style: Clean 2D comic art, 2x2 grid layout, bold outlines, flat colors, European comic book style. "
            f"The word \"{display_text}\" is written as a main title in a bold comic-book banner. "
            f"Educational and clear. High quality. White borders between panels.\n"
            f"{'-'*40}"
        )
        prompts.append(prompt)
        processed_count += 1
        
        if limit and processed_count >= limit:
            break

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("\n".join(prompts))
    
    print(f"Saved {len(prompts)} prompts to: {output_path}")

if __name__ == "__main__":
    json_file = "assets/data/vocab.json"
    output_file = "genspark_prompts_batch1.txt"
    
    # Generate prompts for all enriched words
    generate_prompts(json_file, output_file)
