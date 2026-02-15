#!/usr/bin/env python3
"""Generate Italian example sentences with Korean translations for vocab.json."""
import json
import random
import re

random.seed(42)

with open('assets/data/vocab.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# ── Article helpers ──
def get_def_art(word, gender_info):
    vowels = 'aeiouàèéìòù'
    sv = word[0].lower() in vowels if word else False
    sz = word[0].lower() == 'z' or word[:2].lower() in ('sc','sp','st','sb','sf','sm','sn','sq','gn','pn','ps')
    if 's.f' in gender_info:
        return "l'" if sv else "la "
    else:
        if sv: return "l'"
        if sz: return "lo "
        return "il "

def get_indef_art(word, gender_info):
    vowels = 'aeiouàèéìòù'
    sv = word[0].lower() in vowels if word else False
    sz = word[0].lower() == 'z' or word[:2].lower() in ('sc','sp','st','sb','sf','sm','sn','sq','gn','pn','ps')
    if 's.f' in gender_info:
        return "un'" if sv else "una "
    else:
        if sz: return "uno "
        return "un "

# ── Verb: simple present io/lui ──
def conj_io(v):
    for sfx in ('arsi','ersi','irsi'):
        if v.endswith(sfx):
            base = v[:-len(sfx)]
            return f"mi {base}{'o' if sfx=='arsi' else 'o'}"
    if v.endswith('are'): return v[:-3]+'o'
    if v.endswith('ere'): return v[:-3]+'o'
    if v.endswith('ire'): return v[:-3]+'o'
    if v.endswith('rre'): return v[:-3]+'co'
    return v

def conj_lui(v):
    for sfx in ('arsi','ersi','irsi'):
        if v.endswith(sfx):
            base = v[:-len(sfx)]
            return f"si {base}{'a' if sfx=='arsi' else 'e'}"
    if v.endswith('are'): return v[:-3]+'a'
    if v.endswith('ere'): return v[:-3]+'e'
    if v.endswith('ire'): return v[:-3]+'e'
    if v.endswith('rre'): return v[:-3]+'ce'
    return v

def conj_passato(v):
    """Passato prossimo participle."""
    for sfx in ('arsi','ersi','irsi'):
        if v.endswith(sfx):
            base = v[:-len(sfx)]
            if sfx=='arsi': return f"{base}ato"
            if sfx=='ersi': return f"{base}uto"
            return f"{base}ito"
    if v.endswith('are'): return v[:-3]+'ato'
    if v.endswith('ere'): return v[:-3]+'uto'
    if v.endswith('ire'): return v[:-3]+'ito'
    if v.endswith('rre'): return v[:-3]+'tto'
    return v

# ── Meaning cleaner ──
def clean(meaning):
    m = re.sub(r'\s*\(.*?\)', '', meaning).strip()
    if not m: m = meaning
    return m.split(',')[0].strip()

# ── Templates (Italian, Korean) ──
# Verbs transitive
vt = [
    (lambda w,m: f"Devo {w} il documento prima di sera.", lambda w,m: f"저녁 전에 서류를 {m} 해야 한다."),
    (lambda w,m: f"Mi hanno chiesto di {w}.", lambda w,m: f"나에게 {m}라고 요청했다."),
    (lambda w,m: f"È difficile {w} senza aiuto.", lambda w,m: f"도움 없이 {m}기는 어렵다."),
    (lambda w,m: f"Vorrei {w} qualcosa di speciale.", lambda w,m: f"특별한 것을 {m}고 싶다."),
    (lambda w,m: f"Ho imparato a {w} bene.", lambda w,m: f"잘 {m}는 법을 배웠다."),
    (lambda w,m: f"Non è facile {w}.", lambda w,m: f"{m}기가 쉽지 않다."),
    (lambda w,m: f"Puoi {w} per favore?", lambda w,m: f"제발 {m}해 줄 수 있어?"),
]
# Verbs intransitive
vi = [
    (lambda w,m: f"Mi piace {w} la mattina.", lambda w,m: f"아침에 {m}는 것을 좋아한다."),
    (lambda w,m: f"Il bambino comincia a {w}.", lambda w,m: f"아이가 {m}기 시작한다."),
    (lambda w,m: f"Qui si può {w} tranquillamente.", lambda w,m: f"여기서 편하게 {m} 수 있다."),
    (lambda w,m: f"Ieri ho continuato a {w}.", lambda w,m: f"어제 계속 {m}았다."),
]
# Verbs reflexive
vr = [
    (lambda w,m: f"Bisogna {w} ogni mattina.", lambda w,m: f"매일 아침 {m} 해야 한다."),
    (lambda w,m: f"Mi piace {w} presto.", lambda w,m: f"일찍 {m}는 것을 좋아한다."),
    (lambda w,m: f"È ora di {w}.", lambda w,m: f"{m}할 시간이다."),
]
# Nouns
nm = [
    (lambda w,a,ia,m: f"Hai visto {a}{w}?", lambda w,a,ia,m: f"{m}을(를) 봤어?"),
    (lambda w,a,ia,m: f"Ho bisogno di {ia}{w} nuovo.", lambda w,a,ia,m: f"새 {m}이(가) 필요하다."),
    (lambda w,a,ia,m: f"Questo {w} è davvero bello.", lambda w,a,ia,m: f"이 {m}은(는) 정말 멋지다."),
    (lambda w,a,ia,m: f"Non conosco questo {w}.", lambda w,a,ia,m: f"이 {m}을(를) 모른다."),
    (lambda w,a,ia,m: f"Mi piace molto {a}{w}.", lambda w,a,ia,m: f"나는 {m}이(가) 매우 좋다."),
]
nf = [
    (lambda w,a,ia,m: f"Hai visto {a}{w}?", lambda w,a,ia,m: f"{m}을(를) 봤어?"),
    (lambda w,a,ia,m: f"Ho bisogno di {ia}{w} nuova.", lambda w,a,ia,m: f"새 {m}이(가) 필요하다."),
    (lambda w,a,ia,m: f"Questa {w} è molto bella.", lambda w,a,ia,m: f"이 {m}은(는) 매우 아름답다."),
    (lambda w,a,ia,m: f"Non trovo {a}{w}.", lambda w,a,ia,m: f"{m}을(를) 찾지 못한다."),
    (lambda w,a,ia,m: f"Mi piace molto {a}{w}.", lambda w,a,ia,m: f"나는 {m}이(가) 매우 좋다."),
]
# Adjectives
aj = [
    (lambda w,m: f"Questa persona è molto {w}.", lambda w,m: f"이 사람은 매우 {m}."),
    (lambda w,m: f"Il risultato è stato {w}.", lambda w,m: f"결과가 {m}었다."),
    (lambda w,m: f"È una cosa davvero {w}.", lambda w,m: f"정말 {m} 것이다."),
    (lambda w,m: f"Mi sembra troppo {w}.", lambda w,m: f"너무 {m} 것 같다."),
]
# Adverbs
av = [
    (lambda w,m: f"Lui parla {w}.", lambda w,m: f"그는 {m} 말한다."),
    (lambda w,m: f"Bisogna agire {w}.", lambda w,m: f"{m} 행동해야 한다."),
    (lambda w,m: f"Lo ha fatto {w}.", lambda w,m: f"그것을 {m} 했다."),
]
# Prepositions / conjunctions / other
prep = [
    (lambda w,m: f"La parola '{w}' si usa spesso in italiano.", lambda w,m: f"'{w}'는 이탈리아어에서 자주 쓰인다. ({m})"),
]
generic = [
    (lambda w,m: f"Conosci la parola '{w}'?", lambda w,m: f"'{w}'라는 단어를 알아? ({m})"),
    (lambda w,m: f"'{w.title()}' è una parola molto usata.", lambda w,m: f"'{w}'은(는) 많이 쓰이는 단어이다. ({m})"),
]

updated = 0
for item in data:
    meaning = item.get('meaning', '')
    if not meaning:
        continue
    if item.get('example', ''):
        continue  # skip if already has example

    word = item['word']
    gender = item.get('gender', '')
    m = clean(meaning)

    try:
        is_reflex = word.endswith('rsi')
        is_verb = 'v.' in gender
        is_noun_m = 's.m' in gender
        is_noun_f = 's.f' in gender
        is_adj = 'agg' in gender
        is_adv = 'avv' in gender
        is_prep = 'prep' in gender
        is_conj = 'cong' in gender

        # For words that are both adj+noun, prefer adj template
        # For words with multiple types, pick the first matching

        if is_verb and is_reflex:
            it_fn, kr_fn = random.choice(vr)
            it_s, kr_s = it_fn(word, m), kr_fn(word, m)
        elif is_verb and 'intr' in gender:
            it_fn, kr_fn = random.choice(vi)
            it_s, kr_s = it_fn(word, m), kr_fn(word, m)
        elif is_verb:
            it_fn, kr_fn = random.choice(vt)
            it_s, kr_s = it_fn(word, m), kr_fn(word, m)
        elif is_adj and not is_noun_m and not is_noun_f:
            it_fn, kr_fn = random.choice(aj)
            it_s, kr_s = it_fn(word, m), kr_fn(word, m)
        elif is_noun_f:
            art = get_def_art(word, gender)
            iart = get_indef_art(word, gender)
            it_fn, kr_fn = random.choice(nf)
            it_s, kr_s = it_fn(word, art, iart, m), kr_fn(word, art, iart, m)
        elif is_noun_m:
            art = get_def_art(word, gender)
            iart = get_indef_art(word, gender)
            it_fn, kr_fn = random.choice(nm)
            it_s, kr_s = it_fn(word, art, iart, m), kr_fn(word, art, iart, m)
        elif is_adj:
            it_fn, kr_fn = random.choice(aj)
            it_s, kr_s = it_fn(word, m), kr_fn(word, m)
        elif is_adv:
            it_fn, kr_fn = random.choice(av)
            it_s, kr_s = it_fn(word, m), kr_fn(word, m)
        elif is_prep or is_conj:
            it_fn, kr_fn = random.choice(prep)
            it_s, kr_s = it_fn(word, m), kr_fn(word, m)
        else:
            it_fn, kr_fn = random.choice(generic)
            it_s, kr_s = it_fn(word, m), kr_fn(word, m)

        item['example'] = f"{it_s}\n({kr_s})"
        updated += 1
    except Exception as e:
        print(f"Error for '{word}': {e}")

with open('assets/data/vocab.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Updated {updated} words with examples.")
