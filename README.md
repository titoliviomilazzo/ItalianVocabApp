# Italiano 2000 - 이탈리아어 단어장 앱

개인 학습용 이탈리아어 2,000 단어 플래시카드 앱입니다.

**Live Demo:** https://titoliviomilazzo.github.io/ItalianVocabApp/

## 주요 기능

- **플래시카드 학습**: 4컷 만화 이미지와 함께 단어 암기 (3D 플립 애니메이션)
- **퀴즈 모드**: 4지선다 퀴즈 (20문제 세션, 점수 및 결과 표시)
- **TTS 발음**: 이탈리아어 원어민 발음 재생 (Web Speech API)
- **단어 검색**: 이탈리아어/한국어로 검색
- **학습 통계**: 레벨별 진행률, 전체 학습 대시보드
- **난이도 필터링**: Fondamentale / Alto Uso / Alta Disponibilità
- **셔플 학습**: 순서대로 또는 랜덤 셔플 선택
- **학습 완료 표시**: 단어별 학습 완료 체크

## 기술 스택

- **Framework:** Flutter (Web)
- **Hosting:** GitHub Pages
- **Data:** 로컬 JSON (`assets/data/vocab.json`)
- **이미지:** Genspark Pro로 생성한 4컷 만화 (PNG)
- **TTS:** Web Speech API (`dart:js_interop` + `package:web`)

## 프로젝트 구조

```
lib/
├── main.dart                  # 앱 진입점, 데이터 로딩
├── models/
│   └── word.dart              # 단어 데이터 모델
├── screens/
│   ├── home_screen.dart       # 홈 화면 (검색, 단어 목록)
│   ├── flashcard_screen.dart  # 플래시카드 학습 화면
│   ├── quiz_screen.dart       # 퀴즈 모드 화면
│   └── stats_screen.dart      # 학습 통계 화면
├── widgets/
│   └── flashcard_widget.dart  # 3D 플립 플래시카드 위젯
└── services/
    ├── tts_service.dart       # TTS 발음 서비스
    └── storage_service.dart   # 학습 상태 저장
assets/
├── data/vocab.json            # 2,000 단어 데이터
└── images/                    # 4컷 만화 이미지 (PNG)
scripts/
├── generate_prompts.py        # Genspark 이미지 프롬프트 생성
├── batch2_data.py ~ batch4_data.py  # 단어 데이터 보강 스크립트
└── fix_image_paths.py         # 이미지 경로 매칭 스크립트
```

## 데이터 보강 현황

| Batch | ID 범위 | 한국어 뜻 | 스토리 | 이미지 |
|-------|---------|----------|--------|--------|
| 1 | 1-100 | 완료 | 완료 | 완료 (100개) |
| 2 | 101-200 | 완료 | 완료 | 생성 중 |
| 3 | 201-300 | 완료 | 완료 | 프롬프트 생성 완료 |
| 4 | 301-400 | 완료 | 완료 | 프롬프트 생성 완료 |
| 5-20 | 401-2000 | 미시작 | 미시작 | 미시작 |

## 로컬 개발

```bash
flutter pub get
flutter run -d chrome
```

## 배포

```bash
# C: 드라이브에서 빌드 (Google Drive 한글 경로 이슈 우회)
flutter build web --base-href "/ItalianVocabApp/" --release

# gh-pages 브랜치에 푸시하면 자동 배포
```
