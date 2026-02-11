"""
Fix image_path in vocab.json to match actual filenames in assets/images/.

Actual files: 001_a_alphabet.png, 002_a_roma.png, ...
vocab.json currently has: assets/images/1.webp, assets/images/2.webp, ...

Strategy: Map by ID number. File "001_..." maps to vocab ID 1.
"""
import json
import os
import re

def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    vocab_path = os.path.join(base_dir, "assets", "data", "vocab.json")
    images_dir = os.path.join(base_dir, "assets", "images")

    # Build mapping: id_number -> actual_filename
    id_to_filename = {}
    for fname in os.listdir(images_dir):
        match = re.match(r'^(\d+)_', fname)
        if match:
            file_id = int(match.group(1))
            id_to_filename[file_id] = fname

    print(f"Found {len(id_to_filename)} image files")

    # Update vocab.json
    with open(vocab_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    updated = 0
    for item in data:
        item_id = item['id']
        if item_id in id_to_filename:
            new_path = f"assets/images/{id_to_filename[item_id]}"
            if item.get('image_path') != new_path:
                item['image_path'] = new_path
                updated += 1

    with open(vocab_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"Updated {updated} image paths in vocab.json")
    
    # Show first 5 mappings for verification
    for i in range(1, 6):
        if i in id_to_filename:
            print(f"  ID {i}: assets/images/{id_to_filename[i]}")

if __name__ == "__main__":
    main()
