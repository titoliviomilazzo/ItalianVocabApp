import json
import os

def update_vocab(json_path, updates):
    """
    updates: dict mapping id (int) to dict of fields to update
    example: {1: {"meaning": "...", "story": "..."}}
    """
    if not os.path.exists(json_path):
        print(f"Error: {json_path} not found.")
        return

    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    updated_count = 0
    for item in data:
        item_id = item.get('id')
        if item_id in updates:
            item.update(updates[item_id])
            updated_count += 1

    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print(f"Successfully updated {updated_count} items in {json_path}")

if __name__ == "__main__":
    # Example usage (to be called by other scripts or manually)
    pass
