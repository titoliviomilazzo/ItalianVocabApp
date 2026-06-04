"""Generate Genspark image prompts for batch 5 (IDs 355-404, 50 words)"""
import json, os, re, sys, io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
vocab_path = os.path.join(project_root, 'assets', 'data', 'vocab.json')

with open(vocab_path, 'r', encoding='utf-8') as f:
    vocab = json.load(f)

# Parse existing prompt files for reusable stories
def parse_prompts(filepath):
    data = {}
    if not os.path.exists(filepath):
        return data
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    blocks = content.split('----------------------------------------')
    for block in blocks:
        id_match = re.search(r'Image ID:\s*(\d+)', block)
        word_match = re.search(r'Word:\s*(.+)', block)
        story_match = re.search(r'Story:\s*(.+)', block)
        if id_match and word_match and story_match:
            eid = int(id_match.group(1))
            data[eid] = {
                'word': word_match.group(1).strip(),
                'story': story_match.group(1).strip(),
            }
    return data

existing = parse_prompts(os.path.join(project_root, 'genspark_prompts_batch4.txt'))

# New stories for words not in existing prompts
new_stories = {
    401: '1. Listening to jazz music with closed eyes. 2. Collecting rare vinyl records. 3. Attending every concert of a favorite band. 4. A passionate fan devoted to music.',
    402: '1. A courtroom with a judge at the bench. 2. A lawyer making a final plea. 3. Calling out names from a list. 4. An appeal for justice heard by all.',
    403: '1. The alarm clock ringing at dawn. 2. Eyes barely open, still half asleep. 3. Just barely catching the train. 4. Arriving just in time, barely making it.',
    404: '1. A coat hanging on a hook by the door. 2. A picture frame hung on the wall. 3. Laundry hanging on a clothesline. 4. Hanging things up neatly in the closet.',
}

# Fill meanings for 401-404 in vocab.json
new_meanings = {
    401: {'meaning': '열정적인, 열광적인', 'gender': 'p.pass., agg., s.m.', 'story': new_stories[401]},
    402: {'meaning': '호소, 호명, 항소', 'gender': 's.m.', 'story': new_stories[402]},
    403: {'meaning': '겨우, ~하자마자', 'gender': 'avv., cong.', 'story': new_stories[403]},
    404: {'meaning': '걸다, 매달다', 'gender': 'v.tr.', 'story': new_stories[404]},
}

for eid, data in new_meanings.items():
    for entry in vocab:
        if entry['id'] == eid:
            if not entry['meaning']:
                entry['meaning'] = data['meaning']
            if not entry.get('story'):
                entry['story'] = data['story']
            if not entry.get('gender'):
                entry['gender'] = data['gender']
            break

with open(vocab_path, 'w', encoding='utf-8') as f:
    json.dump(vocab, f, ensure_ascii=False, indent=2)

# Generate prompt file
output_path = os.path.join(project_root, 'genspark_prompts_batch5.txt')
lines = []

for entry in vocab:
    if 355 <= entry['id'] <= 404:
        eid = entry['id']
        word = entry['word']
        gender = entry['gender']

        # Get story: from existing prompts or vocab or new
        if eid in existing:
            story = existing[eid].get('story', '')
        elif entry.get('story'):
            story = entry.get('story', '')
        elif eid in new_stories:
            story = new_stories[eid]
        else:
            story = ''

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

with open(output_path, 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines) + '\n')

print(f'Generated {len(lines)} prompts to {output_path}')
print(f'ID range: 355-404')
