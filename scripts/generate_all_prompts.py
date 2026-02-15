"""
Generate Genspark image prompts for ALL remaining words (IDs 405-7244).
Batches of 50 words each, starting from batch6.
"""
import json, os, re, sys, io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
vocab_path = os.path.join(project_root, 'assets', 'data', 'vocab.json')

with open(vocab_path, 'r', encoding='utf-8') as f:
    vocab = json.load(f)

# === POS-based story templates ===
# These create generic but meaningful 4-panel stories based on part of speech.
# Genspark will interpret the Italian word in context.

def classify_pos(gender):
    """Classify part of speech from gender field."""
    g = gender.lower()
    if 'v.tr' in g or 'v.intr' in g or 'v.rifl' in g:
        return 'verb'
    elif 'avv' in g:
        return 'adverb'
    elif 'agg' in g and ('s.m' in g or 's.f' in g):
        return 'adj_noun'
    elif 'agg' in g:
        return 'adjective'
    elif 'p.pass' in g or 'p.pres' in g:
        return 'participle'
    elif 'cong' in g:
        return 'conjunction'
    elif 'prep' in g:
        return 'preposition'
    elif 'pron' in g:
        return 'pronoun'
    elif 'inter' in g:
        return 'interjection'
    elif 's.m' in g or 's.f' in g:
        return 'noun'
    else:
        return 'noun'  # default

def generate_story(word, gender):
    """Generate a 4-panel story description for image generation."""
    pos = classify_pos(gender)
    w = word

    if pos == 'verb':
        return (
            f"1. A person thinking about the action of '{w}'. "
            f"2. Starting to perform the action '{w}'. "
            f"3. Actively doing '{w}' with full effort. "
            f"4. Successfully completing the action '{w}' with satisfaction."
        )
    elif pos == 'adjective':
        return (
            f"1. Seeing something that is clearly '{w}'. "
            f"2. Comparing two things, one is '{w}' and one is not. "
            f"3. A person pointing at something '{w}' and explaining. "
            f"4. A memorable example of something very '{w}'."
        )
    elif pos == 'adj_noun' or pos == 'participle':
        return (
            f"1. Encountering someone or something described as '{w}'. "
            f"2. Recognizing the quality of '{w}' in a scene. "
            f"3. A vivid example showing '{w}' clearly. "
            f"4. Understanding the full meaning of '{w}'."
        )
    elif pos == 'adverb':
        return (
            f"1. A scene where something happens '{w}'. "
            f"2. Showing the manner or degree of '{w}'. "
            f"3. Contrasting doing something '{w}' vs not. "
            f"4. A clear example of '{w}' in action."
        )
    elif pos in ('conjunction', 'preposition', 'pronoun', 'interjection'):
        return (
            f"1. Two speech bubbles connected by the word '{w}'. "
            f"2. A sentence on a blackboard highlighting '{w}'. "
            f"3. A teacher explaining the use of '{w}'. "
            f"4. Students practicing sentences with '{w}'."
        )
    else:  # noun
        return (
            f"1. Discovering '{w}' for the first time. "
            f"2. Seeing '{w}' in its natural context. "
            f"3. A person interacting with '{w}'. "
            f"4. '{w}' playing an important role in a scene."
        )

# === Generate all prompt files ===
BATCH_SIZE = 50
START_ID = 405
START_BATCH = 6

# Filter remaining words
remaining = [e for e in vocab if e['id'] >= START_ID]
remaining.sort(key=lambda e: e['id'])

print(f"Total words to process: {len(remaining)}")
print(f"Batches needed: {(len(remaining) + BATCH_SIZE - 1) // BATCH_SIZE}")

total_prompts = 0

for batch_idx in range((len(remaining) + BATCH_SIZE - 1) // BATCH_SIZE):
    batch_num = START_BATCH + batch_idx
    batch_words = remaining[batch_idx * BATCH_SIZE : (batch_idx + 1) * BATCH_SIZE]

    if not batch_words:
        break

    id_start = batch_words[0]['id']
    id_end = batch_words[-1]['id']

    lines = []
    for entry in batch_words:
        eid = entry['id']
        word = entry['word']
        gender = entry['gender']

        # Get or generate story
        story = entry.get('story', '')
        if not story:
            story = generate_story(word, gender)

        # Parse story into 4 panels
        panels = re.findall(r'\d+\.\s*(.+?)(?=\s*\d+\.|$)', story)
        while len(panels) < 4:
            panels.append('...')

        block = f"""Image ID: {eid}
Word: {word}
Story: {story}
Prompt: A 4-panel grid comic strip telling a story for the word '{word}'.
Panel 1: {panels[0].strip().rstrip('.')}
Panel 2: {panels[1].strip().rstrip('.')}
Panel 3: {panels[2].strip().rstrip('.')}
Panel 4: {panels[3].strip().rstrip('.')}
Style: Clean 2D comic art, 2x2 grid layout, bold outlines, flat colors, European comic book style. The word "{word} ({gender})" is written as a main title in a bold comic-book banner. Educational and clear. High quality. White borders between panels. Do NOT include any numbers, digits, or numbering in the panels.
----------------------------------------"""
        lines.append(block)

    output_path = os.path.join(project_root, f'genspark_prompts_batch{batch_num}.txt')
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines) + '\n')

    total_prompts += len(lines)
    print(f"Batch {batch_num}: IDs {id_start}-{id_end} ({len(lines)} prompts) -> {os.path.basename(output_path)}")

print(f"\nDone! Generated {total_prompts} prompts across {batch_idx + 1} batch files.")
print(f"Batch files: genspark_prompts_batch{START_BATCH}.txt through genspark_prompts_batch{START_BATCH + batch_idx}.txt")
