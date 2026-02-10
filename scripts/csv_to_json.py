import pandas as pd
import json
import os

def csv_to_json(csv_path, json_path):
    print(f"Reading CSV from: {csv_path}")
    try:
        df = pd.read_csv(csv_path)
    except FileNotFoundError:
        print(f"Error: File not found at {csv_path}")
        return

    vocab_list = []
    
    # Iterate through rows and map columns
    for index, row in df.iterrows():
        # Handle potential NaN values
        word = str(row['Parola']).strip() if pd.notna(row['Parola']) else ""
        if not word: continue # Skip empty words

        vocab_item = {
            "id": int(row['Row']) if pd.notna(row['Row']) else index + 1,
            "word": word,
            "gender": str(row['Parti del discorso']).strip() if pd.notna(row['Parti del discorso']) else "",
            "level": str(row['Tipo']).strip() if pd.notna(row['Tipo']) else "",
            "meaning": "", # Placeholder
            "pronunciation": "", # Placeholder
            # Use 'Row' for ID because it seems consistent in CSV
            "image_path": f"assets/images/{int(row['Row']) if pd.notna(row['Row']) else index + 1}.webp"
        }
        vocab_list.append(vocab_item)

    print(f"Converted {len(vocab_list)} items.")

    # Save to JSON
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(vocab_list, f, ensure_ascii=False, indent=2)
    
    print(f"Saved JSON to: {json_path}")

if __name__ == "__main__":
    csv_file = "Nuovo Vocabolario di Base - Main.csv"
    json_file = "assets/data/vocab.json"
    
    # Ensure directory exists
    os.makedirs(os.path.dirname(json_file), exist_ok=True)
    
    csv_to_json(csv_file, json_file)
