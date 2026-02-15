"""
Update vocab.json for IDs 255-354:
1. Replace words with image file words
2. Extract story/gender from prompt files
3. Fill Korean meanings
"""
import json, os, re, subprocess

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
vocab_path = os.path.join(project_root, 'assets', 'data', 'vocab.json')
images_dir = os.path.join(project_root, 'assets', 'images')

# === Load vocab ===
with open(vocab_path, 'r', encoding='utf-8') as f:
    vocab = json.load(f)

# === Build image mapping for IDs 255-354 ===
image_map = {}
for f in sorted(os.listdir(images_dir)):
    m = re.match(r'(\d+)_(.+)\.png', f)
    if m:
        img_id = int(m.group(1))
        if 255 <= img_id <= 354:
            word = m.group(2)
            display_word = 'animale' if word == 'animale_agg' else word
            image_map[img_id] = (display_word, f)

print(f'Images to process: {len(image_map)}')

# === Parse prompt files for story/gender ===
def parse_prompts(filepath):
    data = {}
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    blocks = content.split('----------------------------------------')
    for block in blocks:
        id_match = re.search(r'Image ID:\s*(\d+)', block)
        word_match = re.search(r'Word:\s*(.+)', block)
        story_match = re.search(r'Story:\s*(.+)', block)
        # Extract gender from Style line: "word (gender)"
        gender_match = re.search(r'The word "[\w\s]+ \(([^)]+)\)"', block)
        if id_match and word_match:
            eid = int(id_match.group(1))
            data[word_match.group(1).strip().lower()] = {
                'story': story_match.group(1).strip() if story_match else '',
                'gender': gender_match.group(1).strip() if gender_match else '',
            }
    return data

prompt3 = parse_prompts(os.path.join(project_root, 'genspark_prompts_batch3.txt'))
prompt4 = parse_prompts(os.path.join(project_root, 'genspark_prompts_batch4.txt'))
prompt_data = {**prompt3, **prompt4}
print(f'Prompt data entries: {len(prompt_data)}')

# === Also load batch3_data.py and batch4_data.py for meaning reuse ===
def load_batch(path):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    ns = {}
    mock = 'enrich_util=type("m",(object,),{"run_enrichment":lambda *a,**k:None})()'
    exec(content.replace('import enrich_util', mock).replace('sys.path.append(os.path.dirname(os.path.abspath(__file__)))', ''), ns)
    return ns.get('updates', {})

# Get old vocab word mapping
result = subprocess.run(['git', 'show', 'HEAD:assets/data/vocab.json'],
    capture_output=True, text=True, cwd=project_root, encoding='utf-8')
old_vocab = json.loads(result.stdout)
old_id_to_word = {e['id']: e['word'] for e in old_vocab if 200 <= e['id'] <= 400}

scripts_dir = os.path.dirname(os.path.abspath(__file__))
batch3 = load_batch(os.path.join(scripts_dir, 'batch3_data.py'))
batch4 = load_batch(os.path.join(scripts_dir, 'batch4_data.py'))

# Build word -> meaning from batch data
batch_meanings = {}
for old_id, data in {**batch3, **batch4}.items():
    if old_id in old_id_to_word:
        batch_meanings[old_id_to_word[old_id].lower()] = data.get('meaning', '')

# === Korean meanings for new words ===
korean_meanings = {
    'alluce': '엄지발가락',
    'alludere': '암시하다, 넌지시 말하다',
    'alluminio': '알루미늄',
    'allungare': '늘이다, 연장하다',
    'alluvione': '홍수, 범람',
    'almeno': '적어도, 최소한',
    'alquanto': '상당히, 꽤',
    'altalena': '그네, 시소',
    'altamente': '매우, 높이',
    'altare': '제단',
    'alterare': '변질시키다, 변경하다',
    'alternare': '번갈아 하다, 교대하다',
    'alternativa': '대안, 선택지',
    'alternativo': '대안의, 대체의',
    'alterno': '교대의, 번갈아 하는',
    'altezza': '높이, 키',
    'alto': '높은, 키가 큰',
    'altoatesino': '알토아디제의 (남티롤)',
    'altopiano': '고원',
    'altrettanto': '마찬가지로, 똑같이',
    'altrimenti': '그렇지 않으면',
    'altro': '다른, 또 다른',
    'altrove': '다른 곳에',
    'altrui': '남의, 타인의',
    'alunno': '학생, 생도',
    'alveare': '벌집',
    'alzare': '들어올리다, 올리다',
    'amante': '연인, 애인',
    'amare': '사랑하다',
    'amaro': '쓴, 씁쓸한',
    'amato': '사랑받는',
    'ambasciata': '대사관',
    'ambientale': '환경의',
    'ambientare': '배경을 설정하다, 적응시키다',
    'ambiente': '환경, 주변',
    'ambito': '분야, 영역',
    'ambizione': '야망, 포부',
    'ambulanza': '구급차',
    'americano': '미국의, 미국인',
    'amicizia': '우정',
    'amico': '친구',
    'ammaccare': '찌그러뜨리다, 멍들게 하다',
    'ammalarsi': '병에 걸리다',
    'ammalato': '아픈, 병든',
    'ammanettare': '수갑을 채우다',
    'ammassare': '쌓다, 모으다',
    'ammasso': '더미, 무더기',
    'ammazzare': '죽이다, 살해하다',
    'ammettere': '인정하다, 허용하다',
    'amministrativo': '행정의, 관리의',
    'amministratore': '관리자, 행정관',
    'amministrazione': '행정, 관리',
    'ammirare': '감탄하다, 존경하다',
    'ammissione': '입학, 인정',
    'ammobiliare': '가구를 비치하다',
    'ammoniaca': '암모니아',
    'ammorbidente': '섬유유연제',
    'ammucchiare': '쌓아올리다, 퇴적하다',
    'ammuffire': '곰팡이가 피다',
    'amore': '사랑',
    'amoroso': '다정한, 사랑스러운',
    'ampiamente': '넓게, 충분히',
    'ampio': '넓은, 광범위한',
    'amplificatore': '증폭기, 앰프',
    'analcolico': '무알코올의',
    'analfabeta': '문맹의, 문맹자',
    'analisi': '분석',
    'analitico': '분석적인',
    'analizzare': '분석하다',
    'analogo': '유사한, 비슷한',
    'ananas': '파인애플',
    'anarchico': '무정부주의의',
    'anatra': '오리',
    'anche': '~도, 또한',
    'anconetano': '안코나의, 안코나 사람',
    'ancora': '아직, 여전히',
    'ancorare': '닻을 내리다, 고정하다',
    'andamento': '추이, 경과',
    'andare': '가다',
    'andata': '가는 길, 편도',
    'anello': '반지, 고리',
    'angelo': '천사',
    'angolare': '모서리의, 각의',
    'angolo': '모퉁이, 각도',
    'angoscia': '고뇌, 불안',
    'anima': '영혼, 정신',
    'animale': '동물',
    'animare': '활기를 띠게 하다',
    'animato': '활기찬, 생기있는',
    'animo': '마음, 용기',
    'annacquare': '물을 타다, 희석하다',
    'annaffiare': '물을 주다',
    'annebbiare': '안개가 끼다, 흐려지다',
    'anniversario': '기념일',
    'anno': '해, 년',
    'annodare': '매듭짓다',
    'annoiare': '지루하게 하다',
    'annotare': '메모하다, 기록하다',
    'annuale': '연간의, 매년의',
}

# === Update vocab.json ===
id_to_idx = {e['id']: i for i, e in enumerate(vocab)}
changed = 0
kept = 0

for img_id, (img_word, img_fname) in sorted(image_map.items()):
    if img_id not in id_to_idx:
        continue
    idx = id_to_idx[img_id]
    entry = vocab[idx]
    new_image_path = f'assets/images/{img_fname}'

    if entry['word'].lower() == img_word.lower():
        # Same word, just update image path
        entry['image_path'] = new_image_path
        kept += 1
    else:
        # Word changes
        entry['word'] = img_word
        entry['image_path'] = new_image_path
        entry['meaning'] = ''
        entry['story'] = ''
        entry['gender'] = ''
        entry['pronunciation'] = ''
        changed += 1

    # Fill meaning if empty
    w = entry['word'].lower()
    if not entry['meaning']:
        if w in batch_meanings:
            entry['meaning'] = batch_meanings[w]
        elif w in korean_meanings:
            entry['meaning'] = korean_meanings[w]

    # Fill story/gender from prompt data if empty
    if not entry['story'] and w in prompt_data:
        entry['story'] = prompt_data[w]['story']
    if not entry['gender'] and w in prompt_data:
        entry['gender'] = prompt_data[w]['gender']

    # Special case: animale_agg (ID 342) - differentiate from animale (ID 341)
    if img_fname == '342_animale_agg.png' and entry['word'] == 'animale':
        entry['gender'] = 'agg.'
        if not entry['meaning']:
            entry['meaning'] = '동물의, 동물적인'

print(f'Kept (same word): {kept}')
print(f'Changed: {changed}')

# Verify
empty_meanings = [(e['id'], e['word']) for e in vocab if 255 <= e['id'] <= 354 and not e['meaning']]
print(f'Empty meanings remaining: {len(empty_meanings)}')
for eid, w in empty_meanings:
    print(f'  {eid}: {w}')

# Verify image paths
mismatch = 0
for img_id, (img_word, img_fname) in sorted(image_map.items()):
    if img_id in id_to_idx:
        entry = vocab[id_to_idx[img_id]]
        if entry['image_path'] != f'assets/images/{img_fname}':
            mismatch += 1
            print(f'PATH MISMATCH: ID {img_id}')

print(f'Image path mismatches: {mismatch}')

# Save
with open(vocab_path, 'w', encoding='utf-8') as f:
    json.dump(vocab, f, ensure_ascii=False, indent=2)
print('vocab.json saved!')
