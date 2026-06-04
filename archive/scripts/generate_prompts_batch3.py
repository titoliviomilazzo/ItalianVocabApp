import json
import os
import re

def generate_prompts(start_id, end_id, output_file):
    vocab_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "assets", "data", "vocab.json")
    
    with open(vocab_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    prompts = []
    
    for item in data:
        if start_id <= item['id'] <= end_id:
            word = item['word']
            gender = item.get('gender', '')
            story = item.get('story', '')
            
            parts = re.split(r'\d+\.', story)
            panels = [p.strip() for p in parts if p.strip()]
            
            if len(panels) < 4:
                panels = ["Scene A", "Scene B", "Scene C", "Scene D"]

            gender_str = f" ({gender})" if gender else ""
            
            prompt_text = f"""Image ID: {item['id']}
Word: {word}
Story: {story}
Prompt: A 4-panel grid comic strip telling a story for the word '{word}'.
Panel 1: {panels[0]}
Panel 2: {panels[1] if len(panels) > 1 else panels[0]}
Panel 3: {panels[2] if len(panels) > 2 else panels[0]}
Panel 4: {panels[3] if len(panels) > 3 else panels[0]}
Style: Clean 2D comic art, 2x2 grid layout, bold outlines, flat colors, European comic book style. The word "{word}{gender_str}" is written as a main title in a bold comic-book banner. Educational and clear. High quality. White borders between panels.
----------------------------------------
"""
            prompts.append(prompt_text)

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("".join(prompts))
    
    print(f"Generated {len(prompts)} prompts in {output_file}")

if __name__ == "__main__":
    output_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "genspark_prompts_batch3.txt")
    generate_prompts(201, 300, output_path)
