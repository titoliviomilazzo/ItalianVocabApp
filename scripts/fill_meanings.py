import json, subprocess, os, sys

# === Step 1: Load current vocab ===
vocab_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'assets', 'data', 'vocab.json')
with open(vocab_path, 'r', encoding='utf-8') as f:
    vocab = json.load(f)

# === Step 2: Get old vocab for word->ID mapping ===
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
result = subprocess.run(['git', 'show', 'HEAD:assets/data/vocab.json'], capture_output=True, text=True, cwd=project_root, encoding='utf-8')
old_vocab = json.loads(result.stdout)
old_id_to_word = {e['id']: e['word'] for e in old_vocab if 101 <= e['id'] <= 300}

# === Step 3: Extract batch data ===
def load_batch(path):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    ns = {}
    mock = 'enrich_util=type("m",(object,),{"run_enrichment":lambda *a,**k:None})()'
    exec(content.replace('import enrich_util', mock).replace('sys.path.append(os.path.dirname(os.path.abspath(__file__)))', ''), ns)
    return ns.get('updates', {})

scripts_dir = os.path.dirname(os.path.abspath(__file__))
batch2 = load_batch(os.path.join(scripts_dir, 'batch2_data.py'))
batch3 = load_batch(os.path.join(scripts_dir, 'batch3_data.py'))

word_data = {}
for old_id, data in {**batch2, **batch3}.items():
    if old_id in old_id_to_word:
        word_data[old_id_to_word[old_id].lower()] = data

# === Step 4: New data for words not in batch data ===
new_data = {
    'acquavite': {'meaning': '증류주, 브랜디', 'gender': 's.f.', 'story': '1. Harvesting grapes from a vineyard. 2. Distilling them in a copper still. 3. A clear, strong liquid pouring out. 4. Sipping the potent acquavite carefully.'},
    'acquazzone': {'meaning': '폭우, 소나기', 'gender': 's.m.', 'story': '1. Dark clouds gathering suddenly. 2. Heavy rain pouring down. 3. People running for shelter. 4. Streets flooded with rainwater.'},
    'acquedotto': {'meaning': '수도, 수로', 'gender': 's.m.', 'story': '1. Ancient Roman arches stretching across a valley. 2. Water flowing through stone channels. 3. Supplying the city with fresh water. 4. A marvel of ancient engineering.'},
    'acqueo': {'meaning': '물의, 수성의', 'gender': 'agg.', 'story': '1. Looking at a glass of clear liquid. 2. Examining it under a microscope. 3. Water molecules moving freely. 4. An aqueous solution for experiments.'},
    'acquirente': {'meaning': '구매자, 매수인', 'gender': 's.m. e f.', 'story': '1. A house with a For Sale sign. 2. A couple viewing the property. 3. Negotiating the price. 4. The buyer signing the contract.'},
    'acrobazia': {'meaning': '곡예, 묘기', 'gender': 's.f.', 'story': '1. A circus performer on a trapeze. 2. Swinging higher and higher. 3. A triple somersault in the air. 4. Landing perfectly to thunderous applause.'},
    'acustica': {'meaning': '음향학, 음향', 'gender': 's.f.', 'story': '1. A concert hall being designed. 2. Engineers testing sound waves. 3. Adjusting panels on the walls. 4. Perfect acoustics for the orchestra.'},
    'acustico': {'meaning': '음향의, 청각의', 'gender': 'agg.', 'story': '1. A musician holding an acoustic guitar. 2. No electric amplifier needed. 3. The natural sound filling the room. 4. A beautiful acoustic performance.'},
    'acutezza': {'meaning': '예리함, 날카로움', 'gender': 's.f.', 'story': '1. A detective examining clues. 2. Noticing a tiny detail others missed. 3. Connecting the pieces together. 4. Solving the case with sharp insight.'},
    'adagiare': {'meaning': '조심스럽게 눕히다', 'gender': 'v.tr.', 'story': '1. A mother holding a sleeping baby. 2. Walking softly to the crib. 3. Gently laying the baby down. 4. The baby sleeping peacefully.'},
    'adagio': {'meaning': '천천히, 서서히', 'gender': 'avv.', 'story': '1. A pianist at the keyboard. 2. Playing the notes very slowly. 3. Each note lingering in the air. 4. A beautiful, slow melody.'},
    'adattabile': {'meaning': '적응할 수 있는', 'gender': 'agg.', 'story': '1. A chameleon on a green leaf. 2. Moving to a brown branch. 3. Changing color to match. 4. Perfectly adaptable to any environment.'},
    'adattamento': {'meaning': '적응, 각색', 'gender': 's.m.', 'story': '1. A popular novel on a shelf. 2. A film director reading it. 3. Writing a screenplay based on it. 4. The movie adaptation premieres.'},
    'addebitare': {'meaning': '청구하다, 부과하다', 'gender': 'v.tr.', 'story': '1. A waiter bringing the restaurant bill. 2. Checking the charges carefully. 3. Handing over a credit card. 4. The amount debited from the account.'},
    'addebito': {'meaning': '청구, 부과', 'gender': 's.m.', 'story': '1. Opening a bank statement. 2. Seeing an unexpected charge. 3. Calling the bank to inquire. 4. Resolving the billing issue.'},
    'addentare': {'meaning': '물다, 깨물다', 'gender': 'v.tr.', 'story': '1. Holding a big juicy apple. 2. Opening mouth wide. 3. Biting into it with a crunch. 4. Juice dripping down the chin.'},
    'addestramento': {'meaning': '훈련, 조련', 'gender': 's.m.', 'story': '1. A military training camp. 2. Soldiers running an obstacle course. 3. Practicing drills together. 4. Ready after intense training.'},
    'addestrare': {'meaning': '훈련시키다, 조련하다', 'gender': 'v.tr.', 'story': '1. A dog trainer with a puppy. 2. Teaching it to sit and stay. 3. Rewarding with treats. 4. A well-trained dog obeying commands.'},
    'addiaccio': {'meaning': '야영, 노숙', 'gender': 's.m.', 'story': '1. Shepherds in the mountains at night. 2. Sleeping outdoors under the stars. 3. A campfire keeping them warm. 4. Waking up in the open air.'},
    'addirsi': {'meaning': '어울리다, 적합하다', 'gender': 'v.intr.', 'story': '1. Trying on a formal suit. 2. Looking in the mirror. 3. The color and style fitting perfectly. 4. A look that truly suits the person.'},
    'additivo': {'meaning': '첨가물, 첨가제', 'gender': 's.m.', 'story': '1. Reading a food ingredient label. 2. Seeing chemical names listed. 3. Preservatives and colorings added. 4. Choosing natural food instead.'},
    'addobbo': {'meaning': '장식, 장식물', 'gender': 's.m.', 'story': '1. A Christmas tree waiting to be decorated. 2. Colorful ornaments in a box. 3. Hanging each one carefully. 4. The tree beautifully adorned.'},
    'addome': {'meaning': '복부, 배', 'gender': 's.m.', 'story': '1. A doctor examining a patient. 2. Pressing gently on the abdomen. 3. Checking for any pain. 4. A healthy abdomen confirmed.'},
    'addormentare': {'meaning': '재우다, 잠들게 하다', 'gender': 'v.tr.', 'story': '1. A mother reading a bedtime story. 2. The child listening with heavy eyes. 3. Slowly drifting off to sleep. 4. Tucking the blanket gently.'},
    'addurre': {'meaning': '제시하다, 인용하다', 'gender': 'v.tr.', 'story': '1. A lawyer in a courtroom. 2. Presenting evidence to the judge. 3. Citing legal precedents. 4. Building a strong argument.'},
    'adeguamento': {'meaning': '조정, 적응', 'gender': 's.m.', 'story': '1. New safety regulations announced. 2. A factory reviewing its procedures. 3. Making changes to comply. 4. Successfully adjusted to new standards.'},
    'adeguatamente': {'meaning': '적절하게, 충분히', 'gender': 'avv.', 'story': '1. Preparing for a cold winter hike. 2. Wearing warm layers and boots. 3. Packing enough food and water. 4. Adequately prepared for the journey.'},
    'adempiere': {'meaning': '이행하다, 수행하다', 'gender': 'v.tr.', 'story': '1. Signing a contract at work. 2. Reading the obligations carefully. 3. Completing every task on time. 4. Fulfilling all promises made.'},
    'adempimento': {'meaning': '이행, 수행', 'gender': 's.m.', 'story': '1. A checklist of duties. 2. Completing each one by one. 3. The last item checked off. 4. Full fulfillment of responsibilities.'},
    'aderenza': {'meaning': '밀착, 부착, 지지', 'gender': 's.f.', 'story': '1. Tires on a wet road. 2. Testing their grip. 3. Good traction keeping the car safe. 4. Strong adherence to the surface.'},
    'adescamento': {'meaning': '유인, 유혹', 'gender': 's.m.', 'story': '1. A fisherman preparing bait. 2. Placing it carefully on the hook. 3. Casting the line into the water. 4. A fish drawn to the lure.'},
    'adescare': {'meaning': '유인하다, 미끼로 꾀다', 'gender': 'v.tr.', 'story': '1. A trap set in the forest. 2. Food placed inside as bait. 3. An animal approaching cautiously. 4. Lured by the irresistible scent.'},
    'adesivo': {'meaning': '접착제, 스티커', 'gender': 's.m., agg.', 'story': '1. A child with a sheet of stickers. 2. Peeling one off carefully. 3. Sticking it on a notebook. 4. Colorful adhesive decorations everywhere.'},
    'adiacente': {'meaning': '인접한, 이웃한', 'gender': 'agg.', 'story': '1. Two houses side by side. 2. Sharing a common wall. 3. Neighbors waving from adjacent gardens. 4. The buildings close together.'},
    'adibire': {'meaning': '사용하다, 충당하다', 'gender': 'v.tr.', 'story': '1. An empty room in an office. 2. Deciding to use it as a meeting room. 3. Adding a table and chairs. 4. The room now designated for meetings.'},
    'adipe': {'meaning': '지방, 지방 조직', 'gender': 's.m.', 'story': '1. A biology class studying the body. 2. Diagrams showing fat tissue. 3. Understanding its role as energy storage. 4. Adipose tissue under the skin.'},
    'adiposo': {'meaning': '지방의, 비만한', 'gender': 'agg.', 'story': '1. A doctor reviewing health charts. 2. Measuring body fat percentage. 3. Explaining adipose tissue levels. 4. Recommending diet and exercise.'},
    'adirarsi': {'meaning': '화내다, 격분하다', 'gender': 'v.pronom.intr.', 'story': '1. Someone cutting in line. 2. Face turning red with anger. 3. Clenching fists tightly. 4. Taking deep breaths to calm down.'},
    'adito': {'meaning': '입구, 접근', 'gender': 's.m.', 'story': '1. A narrow passageway in an old castle. 2. Walking through a stone entrance. 3. Discovering a hidden room beyond. 4. The secret entry revealed.'},
    'adombrare': {'meaning': '그늘지게 하다, 암시하다', 'gender': 'v.tr.', 'story': '1. A large tree casting a shadow. 2. A speech hinting at a hidden meaning. 3. A worried look on someone face. 4. Something subtly overshadowed.'},
    'adorabile': {'meaning': '사랑스러운, 귀여운', 'gender': 'agg.', 'story': '1. A tiny puppy with big eyes. 2. A baby laughing joyfully. 3. A kitten playing with yarn. 4. Adorable moments everywhere.'},
    'adorazione': {'meaning': '숭배, 경배', 'gender': 's.f.', 'story': '1. People kneeling in a temple. 2. Candles lit in reverence. 3. Prayers spoken with devotion. 4. Deep adoration and worship.'},
    'adornare': {'meaning': '장식하다, 꾸미다', 'gender': 'v.tr.', 'story': '1. A plain white cake on the table. 2. Adding flowers and ribbons. 3. Piping colorful frosting. 4. A beautifully adorned masterpiece.'},
    'adorno': {'meaning': '장식된, 꾸며진', 'gender': 'agg.', 'story': '1. A palace hall with gold trim. 2. Walls covered in paintings. 3. Crystal chandeliers hanging above. 4. A room richly adorned.'},
    'adottivo': {'meaning': '입양의, 양자의', 'gender': 'agg.', 'story': '1. A couple visiting an orphanage. 2. Meeting a child for the first time. 3. Signing adoption papers. 4. A new adoptive family together.'},
    'adulare': {'meaning': '아첨하다', 'gender': 'v.tr.', 'story': '1. An employee praising the boss excessively. 2. Compliments that seem too generous. 3. Others rolling their eyes. 4. Flattery with an ulterior motive.'},
    'adulazione': {'meaning': '아첨, 아부', 'gender': 's.f.', 'story': '1. A courtier bowing before the king. 2. Showering with excessive praise. 3. The king suspicious of the flattery. 4. Hollow adulation exposed.'},
    'adulterare': {'meaning': '불순물을 섞다, 변조하다', 'gender': 'v.tr.', 'story': '1. A food inspector checking products. 2. Discovering diluted olive oil. 3. Testing for added chemicals. 4. The adulterated product pulled from shelves.'},
    'adulterio': {'meaning': '간통, 불륜', 'gender': 's.m.', 'story': '1. A couple seemingly happy together. 2. Secret messages on a phone. 3. The truth coming to light. 4. A relationship broken by betrayal.'},
    'adultero': {'meaning': '간통자', 'gender': 'agg., s.m.', 'story': '1. A person leading a double life. 2. Sneaking around in secret. 3. Eventually caught by evidence. 4. Facing the consequences of betrayal.'},
    'adunanza': {'meaning': '집회, 모임', 'gender': 's.f.', 'story': '1. A town hall with seats filling up. 2. Citizens gathering for a meeting. 3. A speaker at the podium. 4. Important decisions made together.'},
    'adunare': {'meaning': '모으다, 집합시키다', 'gender': 'v.tr.', 'story': '1. A general summoning troops. 2. Soldiers assembling in the square. 3. Standing in formation. 4. All gathered and ready.'},
    'adunata': {'meaning': '집합, 소집', 'gender': 's.f.', 'story': '1. A bugle call at dawn. 2. Soldiers rushing to the courtyard. 3. Roll call by the commander. 4. Everyone assembled for duty.'},
    'adunco': {'meaning': '갈고리 모양의, 구부러진', 'gender': 'agg.', 'story': '1. An eagle with a hooked beak. 2. A curved sword on display. 3. A bent nail on the wall. 4. Everything hooked and curved.'},
    'aerare': {'meaning': '환기하다, 통풍시키다', 'gender': 'v.tr.', 'story': '1. A stuffy room with closed windows. 2. Opening them wide. 3. Fresh air flowing in. 4. The room feeling clean and fresh.'},
    'aerazione': {'meaning': '환기, 통풍', 'gender': 's.f.', 'story': '1. A ventilation system in a building. 2. Air ducts running along the ceiling. 3. Fans pushing fresh air through. 4. Good aeration for comfort.'},
    'aeronautica': {'meaning': '항공학, 공군', 'gender': 's.f.', 'story': '1. Fighter jets on a runway. 2. Pilots in flight suits. 3. An air force base. 4. The aeronautics keeping skies safe.'},
    'aerosol': {'meaning': '에어로졸, 분무기', 'gender': 's.m.', 'story': '1. A can of spray paint. 2. Pressing the nozzle. 3. Fine mist spraying out. 4. An aerosol cloud of color.'},
    'affabile': {'meaning': '상냥한, 친절한', 'gender': 'agg.', 'story': '1. Meeting a new neighbor. 2. They greet with a warm smile. 3. Offering tea and conversation. 4. An affable and friendly person.'},
    'affaccendarsi': {'meaning': '분주히 움직이다', 'gender': 'v.pronom.intr.', 'story': '1. A chef in a busy kitchen. 2. Running between stoves and counters. 3. Chopping, stirring, and plating. 4. Bustling to prepare the meal.'},
    'affacciarsi': {'meaning': '(창에) 나타나다, 내다보다', 'gender': 'v.pronom.intr.', 'story': '1. Hearing music from outside. 2. Walking to the balcony. 3. Leaning out to look down. 4. Watching a street performer below.'},
    'affannare': {'meaning': '숨차게 하다, 걱정시키다', 'gender': 'v.tr.', 'story': '1. Running up a steep hill. 2. Breathing getting heavier. 3. Heart pounding fast. 4. Stopping to catch breath.'},
    'affannoso': {'meaning': '숨가쁜, 고통스러운', 'gender': 'agg.', 'story': '1. Climbing the last flight of stairs. 2. Panting heavily. 3. Sweat on the forehead. 4. A breathless and laborious effort.'},
    'affarista': {'meaning': '사업가, 장사꾼', 'gender': 's.m. e f.', 'story': '1. A shrewd dealer at a market. 2. Buying low and selling high. 3. Always looking for the next deal. 4. A profit-driven businessperson.'},
}

# === Step 5: Apply all data ===
filled_batch = 0
filled_new = 0

for entry in vocab:
    if 101 <= entry['id'] <= 254 and not entry['meaning']:
        w = entry['word'].lower()
        if w in word_data:
            entry['meaning'] = word_data[w]['meaning']
            entry['story'] = word_data[w]['story']
            filled_batch += 1
        elif w in new_data:
            entry['meaning'] = new_data[w]['meaning']
            entry['story'] = new_data[w]['story']
            if not entry['gender']:
                entry['gender'] = new_data[w]['gender']
            filled_new += 1
        else:
            print(f'STILL EMPTY: ID {entry["id"]} {entry["word"]}')

# Save
with open(vocab_path, 'w', encoding='utf-8') as f:
    json.dump(vocab, f, ensure_ascii=False, indent=2)

print(f'Filled from batch data: {filled_batch}')
print(f'Filled with new data: {filled_new}')

# Verify
empty_count = sum(1 for e in vocab if 101 <= e['id'] <= 254 and not e['meaning'])
print(f'Remaining empty meanings (101-254): {empty_count}')
