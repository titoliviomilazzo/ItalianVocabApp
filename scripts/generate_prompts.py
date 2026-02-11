import json
import re
import sys

# Generate genspark prompts for batches 3-4 (IDs 201-400)
# Fixed: No numbers in panels, all 4 story sentences used as panel descriptions

with open(r'j:\내 드라이브\Code\ItalianVocabApp\assets\data\vocab.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

words = data if isinstance(data, list) else data.get('words', data)

def parse_story(story_text):
    """Parse story into 4 sentences, removing leading numbers like '1. ', '2. ' etc."""
    if not story_text:
        return ['Scene 1', 'Scene 2', 'Scene 3', 'Scene 4']
    
    # Split by numbered pattern "1. ...", "2. ...", etc.
    parts = re.split(r'\d+\.\s+', story_text)
    parts = [p.strip().rstrip('.') for p in parts if p.strip()]
    
    # Ensure exactly 4 panels
    while len(parts) < 4:
        parts.append(f'Scene {len(parts) + 1}')
    
    return parts[:4]

def generate_prompts(start_id, end_id, output_file):
    batch_words = [w for w in words if start_id <= w['id'] <= end_id]
    
    with open(output_file, 'w', encoding='utf-8') as f:
        for w in batch_words:
            word_id = w['id']
            word = w['word']
            gender = w.get('gender', '')
            story = w.get('story', '')
            
            panels = parse_story(story)
            
            f.write(f"Image ID: {word_id}\n")
            f.write(f"Word: {word}\n")
            f.write(f"Story: {story}\n")
            f.write(f"Prompt: A 4-panel grid comic strip telling a story for the word '{word}'.\n")
            f.write(f"Panel 1: {panels[0]}.\n")
            f.write(f"Panel 2: {panels[1]}.\n")
            f.write(f"Panel 3: {panels[2]}.\n")
            f.write(f"Panel 4: {panels[3]}.\n")
            f.write(f"Style: Clean 2D comic art, 2x2 grid layout, bold outlines, flat colors, European comic book style. ")
            f.write(f"The word \"{word} ({gender})\" is written as a main title in a bold comic-book banner. ")
            f.write(f"Educational and clear. High quality. White borders between panels. ")
            f.write(f"Do NOT include any numbers, digits, or numbering in the panels.\n")
            f.write(f"----------------------------------------\n")
    
    print(f"Generated {len(batch_words)} prompts -> {output_file}")

# Generate batch 3 (201-300) and batch 4 (301-400)
generate_prompts(201, 300, r'j:\내 드라이브\Code\ItalianVocabApp\genspark_prompts_batch3.txt')
generate_prompts(301, 400, r'j:\내 드라이브\Code\ItalianVocabApp\genspark_prompts_batch4.txt')

print("Done! Batch 3 and 4 prompt files generated.")
