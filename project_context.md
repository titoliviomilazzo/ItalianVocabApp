# Italiano 2000 - 프로젝트 컨텍스트

## 프로젝트 개요
이탈리아어 2,000 단어 플래시카드 웹앱. Flutter Web으로 개발, GitHub Pages로 배포.

**Live URL:** https://titoliviomilazzo.github.io/ItalianVocabApp/
**GitHub:** https://github.com/titoliviomilazzo/ItalianVocabApp

## 기술 스택
- Framework: Flutter 3.38.9 (Web)
- Hosting: GitHub Pages (gh-pages 브랜치)
- Data: 로컬 JSON (assets/data/vocab.json, 2000개 단어)
- 이미지: Genspark Pro로 생성한 4컷 만화 (PNG)
- TTS: Web Speech API (dart:js_interop + package:web)
- 개발 환경: Windows 11, VS Code, Google Drive (J:\내 드라이브\Code\ItalianVocabApp)

## 구현 완료된 기능
1. **플래시카드 학습**: 4컷 만화 이미지 + 3D 플립 애니메이션, 앞면(이탈리아어+이미지), 뒷면(한글 뜻)
2. **퀴즈 모드**: 4지선다, 20문제 세션, 점수 및 결과 표시
3. **TTS 발음**: 이탈리아어 원어민 발음 재생
4. **단어 검색**: 이탈리아어/한국어로 검색
5. **학습 통계**: 레벨별 진행률, 전체 학습 대시보드
6. **난이도 필터링**: Fondamentale / Alto Uso / Alta Disponibilità
7. **셔플 학습**: 순서대로 또는 랜덤 셔플 선택
8. **학습 완료 표시**: 단어별 학습 완료 체크
9. **네비게이션**: 이전/다음 화살표 버튼, 카드 카운터

## 프로젝트 파일 구조
```
lib/
├── main.dart                  # 앱 진입점, 데이터 로딩 (FutureBuilder)
├── models/
│   └── word.dart              # Word 데이터 모델 (id, word, gender, level, meaning, pronunciation, imagePath, story, isLearned)
├── screens/
│   ├── home_screen.dart       # 홈 화면 (검색바, 단어 목록, 필터, 학습시작/퀴즈 버튼)
│   ├── flashcard_screen.dart  # 플래시카드 학습 화면 (PageView, 셔플, 이전/다음)
│   ├── quiz_screen.dart       # 퀴즈 모드 화면 (4지선다, 20문제)
│   └── stats_screen.dart      # 학습 통계 화면 (원형 진행률, 레벨별 바)
├── widgets/
│   └── flashcard_widget.dart  # 3D 플립 카드 위젯 (AnimationController, Transform rotateY)
└── services/
    ├── tts_service.dart       # Web Speech API TTS 서비스
    └── storage_service.dart   # 학습 상태 저장 (localStorage)
assets/
├── data/vocab.json            # 2,000 단어 데이터
└── images/                    # 4컷 만화 이미지 (PNG, 001_a_alphabet.png 형식)
scripts/
├── generate_prompts.py        # Genspark 이미지 프롬프트 생성 (숫자 없는 버전)
├── batch2_data.py             # Batch 2 데이터 보강 (101-200)
├── batch3_data.py             # Batch 3 데이터 보강 (201-300)
├── batch4_data.py             # Batch 4 데이터 보강 (301-400)
└── fix_image_paths.py         # vocab.json 이미지 경로 매칭
```

## 데이터 보강 현황
| Batch | ID 범위 | 한국어 뜻 | 스토리 | 이미지 | 프롬프트 |
|-------|---------|----------|--------|--------|---------|
| 1 | 1-100 | 완료 | 완료 | 완료 (100개) | batch1 |
| 2 | 101-200 | 완료 | 완료 | 생성 중 | batch2 |
| 3 | 201-300 | 완료 | 완료 | 미시작 | batch3 (숫자 없는 버전) |
| 4 | 301-400 | 완료 | 완료 | 미시작 | batch4 (숫자 없는 버전) |
| 5-20 | 401-2000 | 미시작 | 미시작 | 미시작 | 미시작 |

## 알려진 이슈 & 참고사항
- **Google Drive 경로 이슈**: `J:\내 드라이브\` 한글 경로 때문에 `flutter build web`이 실패함. C:\temp\에 클론해서 빌드해야 함.
- **Android/macOS 플랫폼 파일**: Google Drive 권한 문제로 일부 파일(android/res, macos/xcshareddata) 복구 불가. 웹 앱에는 영향 없음.
- **shared_preferences**: Google Drive symlink 문제로 사용 불가, localStorage로 대체.
- **이미지 프롬프트**: Batch 1-2는 패널에 숫자가 포함되는 문제 있었음. Batch 3부터 "Do NOT include any numbers" 지시 추가.
- **이미지 파일명**: `{id}_{word}.png` 형식 (예: 001_a_alphabet.png)
- **배포 방법**: C:\temp에 클론 → flutter build web --base-href "/ItalianVocabApp/" → gh-pages 브랜치에 푸시

## 다음 할 일 (우선순위)
1. Batch 2 이미지 생성 완료 (Genspark 리밋 대기 중)
2. Batch 3-4 이미지 생성
3. Batch 5+ 데이터 보강 (401-500+)
4. 새 이미지/데이터 추가 후 재배포
5. (선택) 추가 기능: 더 많은 UI 개선, 오프라인 지원 등

## 작업 히스토리 (세션별)
### 세션 1-3 (Antigravity/Gemini)
- 프로젝트 생성, 기본 UI, Batch 1-2 데이터 보강
- 퀴즈 모드, TTS, 이미지 경로 매칭
- Batch 3-4 데이터 보강, 프롬프트 생성

### 세션 4 (Claude Code - 2026-02-11)
- 이전 세션 코드 확인 및 플래시카드 플립 버그 수정 확인
- GitHub에 코드 푸시 (검색, 통계, 카드 애니메이션, 프롬프트 개선)
- Flutter 웹 빌드 및 GitHub Pages 배포
- 아이폰에서 앱 동작 확인 성공
- README 문서 업데이트
