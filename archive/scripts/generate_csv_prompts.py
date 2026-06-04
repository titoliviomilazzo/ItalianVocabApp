#!/usr/bin/env python3
"""
Generate image prompts for B1/B2 CSV words in the same format as existing batches.
Outputs prompt files ready for GenSpark image generation.
Also adds new words to vocab.json and updates existing ones with CSV examples.
"""
import json
import csv
import re
import os

# ── Load existing data ──
with open('assets/data/vocab.json', 'r', encoding='utf-8') as f:
    vocab = json.load(f)

existing_by_word = {}
for item in vocab:
    key = item['word'].lower().strip()
    if key not in existing_by_word:
        existing_by_word[key] = item

max_id = max(item['id'] for item in vocab)

# ── Read CSVs ──
b1 = list(csv.DictReader(open('B1-voca-enriched.csv', 'r', encoding='utf-8-sig')))
b2 = list(csv.DictReader(open('B2-voca-copy-final.csv', 'r', encoding='utf-8-sig')))

# ── Merge and deduplicate ──
merged = {}  # word -> {word, meaning_kr, gender, example_it, example_kr, source}

for row in b1:
    w = row.get('Italian', '').strip()
    if not w:
        continue
    kr = row.get('Korean', '').strip()
    g = row.get('Gender', '').strip()
    ex_it = row.get('Example_IT', '').strip()
    ex_kr = row.get('Example_KR', '').strip()
    key = w.lower()
    if key not in merged:
        merged[key] = {
            'word': w, 'meaning_kr': kr, 'gender_hint': g,
            'example_it': ex_it, 'example_kr': ex_kr, 'source': 'B1'
        }

for row in b2:
    w = row.get('이탈리아어', '').strip()
    if not w:
        continue
    kr = row.get('한국어 뜻', '').strip()
    g = row.get('성별', '').strip()
    ex_it = row.get('예문', '').strip()
    ex_kr = row.get('예문 번역', '').strip()
    key = w.lower()
    if key not in merged:
        merged[key] = {
            'word': w, 'meaning_kr': kr, 'gender_hint': g,
            'example_it': ex_it, 'example_kr': ex_kr, 'source': 'B2'
        }

print(f"Merged unique words: {len(merged)}")

# ── Determine gender string for prompt ──
def infer_gender_label(word, gender_hint, existing_gender=''):
    """Use existing vocab gender if available, otherwise infer from CSV hint."""
    if existing_gender:
        return existing_gender
    w = word.lower()
    gh = gender_hint.lower().strip() if gender_hint else ''
    # Check word endings
    if w.endswith('are') or w.endswith('ere') or w.endswith('ire') or w.endswith('rre') or w.endswith('rsi'):
        if w.endswith('rsi'):
            return 'v.pronom.intr.'
        return 'v.tr.'
    if gh == 'f':
        return 's.f.'
    if gh == 'm':
        return 's.m.'
    # Guess from word ending
    if w.endswith('zione') or w.endswith('tà') or w.endswith('ezza') or w.endswith('ura'):
        return 's.f.'
    if w.endswith('mento') or w.endswith('ismo') or w.endswith('ore'):
        return 's.m.'
    if w.endswith('oso') or w.endswith('ile') or w.endswith('ivo') or w.endswith('ale') or w.endswith('ico'):
        return 'agg.'
    if w.endswith('mente'):
        return 'avv.'
    return 'agg.'

# ── Story templates by word type ──
def generate_story_and_prompt(word, meaning_kr, gender_label):
    """Generate a 4-panel story based on word type and meaning."""
    w = word
    is_verb = 'v.' in gender_label
    is_noun = 's.' in gender_label
    is_adj = 'agg' in gender_label and not is_noun
    is_adv = 'avv' in gender_label

    if is_verb:
        stories = [
            [f"A person facing a situation where they need to {w}.",
             f"Preparing and getting ready to {w}.",
             f"Actively performing the action of {w} with determination.",
             f"The satisfying result after successfully completing {w}."],
            [f"Someone explaining the concept of {w} to a friend.",
             f"A real-life scenario that requires {w}.",
             f"A person in the middle of {w} with focus.",
             f"The positive outcome of {w} shown clearly."],
            [f"A thought bubble showing the idea of {w}.",
             f"Taking the first step to {w}.",
             f"Fully engaged in the act of {w}.",
             f"A completed scene showing the effect of {w}."],
        ]
    elif is_noun:
        stories = [
            [f"A clear depiction of {w} in everyday life.",
             f"Someone encountering {w} for the first time.",
             f"A person using or interacting with {w}.",
             f"{w.title()} playing a key role in a memorable scene."],
            [f"An illustration showing what {w} looks like.",
             f"{w.title()} in its typical environment or context.",
             f"A person pointing at {w} and explaining it.",
             f"A scene where {w} is essential and important."],
            [f"Discovering {w} in an interesting setting.",
             f"Observing {w} up close with curiosity.",
             f"A practical use of {w} in daily life.",
             f"Understanding why {w} matters to people."],
        ]
    elif is_adj:
        stories = [
            [f"Seeing something that is clearly {w}.",
             f"Comparing two things: one is {w}, the other is not.",
             f"A person describing something as {w} with gestures.",
             f"A vivid, memorable example of something very {w}."],
            [f"A scene that perfectly represents the feeling of {w}.",
             f"An object or place that embodies {w}.",
             f"Someone reacting to something {w}.",
             f"The concept of {w} illustrated in a clear way."],
        ]
    elif is_adv:
        stories = [
            [f"A person doing an action normally.",
             f"The same person now doing it {w}.",
             f"The difference is clearly visible.",
             f"Understanding the meaning of {w} through contrast."],
        ]
    else:
        stories = [
            [f"Encountering the concept of '{w}' in daily life.",
             f"Seeing '{w}' used in a natural Italian context.",
             f"A person demonstrating the meaning of '{w}'.",
             f"A clear and memorable example of '{w}' in action."],
        ]

    import random
    random.seed(hash(word))
    story = random.choice(stories)

    story_text = ' '.join(f"{i+1}. {s}" for i, s in enumerate(story))

    prompt_lines = [
        f"Image ID: {{id}}",
        f"Word: {w}",
        f"Story: {story_text}",
        f"Prompt: A 4-panel grid comic strip telling a story for the word '{w}'.",
    ]
    for i, s in enumerate(story):
        prompt_lines.append(f"Panel {i+1}: {s}")

    prompt_lines.append(
        f'Style: Clean 2D comic art, 2x2 grid layout, bold outlines, flat colors, European comic book style. '
        f'The word "{w} ({gender_label})" is written as a main title in a bold comic-book banner. '
        f'Educational and clear. High quality. White borders between panels. '
        f'Do NOT include any numbers, digits, or numbering in the panels.'
    )

    return story_text, '\n'.join(prompt_lines)


# ── Process all words ──
prompts = []
new_vocab_entries = []
updated_existing = 0
next_id = max_id + 1

for key, info in sorted(merged.items()):
    word = info['word']
    meaning_kr = info['meaning_kr']
    example_it = info['example_it']
    example_kr = info['example_kr']

    # Check if already in vocab
    if key in existing_by_word:
        existing = existing_by_word[key]
        word_id = existing['id']
        gender_label = existing.get('gender', '')

        # Update existing entry with CSV data if it improves it
        if meaning_kr and not existing.get('meaning', ''):
            existing['meaning'] = meaning_kr
        if example_it and example_kr:
            # Use the real CSV example (better than template-generated)
            existing['example'] = f"{example_it}\n({example_kr})"
            updated_existing += 1
    else:
        # New word - assign new ID
        word_id = next_id
        next_id += 1
        gender_label = infer_gender_label(word, info['gender_hint'])

        new_entry = {
            'id': word_id,
            'word': word,
            'gender': gender_label,
            'level': f"CSV-{info['source']}",
            'meaning': meaning_kr,
            'pronunciation': '',
            'image_path': f"assets/images/{word_id}_{re.sub(r'[^a-zA-Z0-9]', '_', word.lower())}.jpg",
            'story': '',
        }
        if example_it and example_kr:
            new_entry['example'] = f"{example_it}\n({example_kr})"
        else:
            new_entry['example'] = ''

        new_vocab_entries.append(new_entry)
        vocab.append(new_entry)
        existing_by_word[key] = new_entry

    # Generate prompt
    gender_label = existing_by_word[key].get('gender', '') or infer_gender_label(word, info['gender_hint'])
    _, prompt_text = generate_story_and_prompt(word, meaning_kr, gender_label)
    prompt_text = prompt_text.replace('{id}', str(word_id))
    prompts.append(prompt_text)

# ── Save updated vocab.json ──
with open('assets/data/vocab.json', 'w', encoding='utf-8') as f:
    json.dump(vocab, f, ensure_ascii=False, indent=2)

print(f"Updated {updated_existing} existing entries with CSV examples")
print(f"Added {len(new_vocab_entries)} new words to vocab.json")
print(f"Total prompts generated: {len(prompts)}")

# ── Write prompt files in batches of 50 ──
BATCH_SIZE = 50
separator = "\n" + "-" * 40 + "\n"

for batch_idx in range(0, len(prompts), BATCH_SIZE):
    batch = prompts[batch_idx:batch_idx + BATCH_SIZE]
    batch_num = (batch_idx // BATCH_SIZE) + 1
    filename = f"csv_prompts_batch{batch_num}.txt"

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(separator.join(batch))
        f.write('\n')

    # Get ID range for this batch
    first_line = batch[0].split('\n')[0]
    last_line = batch[-1].split('\n')[0]
    print(f"  {filename}: {len(batch)} prompts ({first_line} ~ {last_line})")

print(f"\nDone! {len(prompts)} prompts written to {(len(prompts)-1)//BATCH_SIZE + 1} batch files.")
