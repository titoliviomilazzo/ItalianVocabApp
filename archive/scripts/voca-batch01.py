import pandas as pd

# 배치로 제공받은 데이터를 리스트에 추가
data = [
    {"word": "Consapevolezza", "gender": "f.", "level": "B2.1", "meaning": "인식, 의식"},
    {"word": "Abitudine", "gender": "f.", "level": "B1.1", "meaning": "습관"},
    # ... 추가 데이터
]

def save_to_markdown(data, filename="ita_vocab_2000.md"):
    df = pd.DataFrame(data)
    with open(filename, 'w', encoding='utf-8') as f:
        f.write("# 이탈리아어 2000 단어장\n\n")
        f.write(df.to_markdown(index=False))
    print(f"저장 완료: {filename}")

# 활용 예시
save_to_markdown(data)