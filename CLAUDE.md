# CLAUDE.md

## 프로젝트 개요
- 프로젝트: `Dammi Parole` (Italian vocabulary learning app)
- 플랫폼: Flutter Web PWA
- 배포: GitHub Pages (`/ItalianVocabApp/`)

## 현재 기준 스택
- Flutter: `3.38.9`
- Dart SDK: `^3.10.8`
- TTS: Web Speech API 기반 (`package:web` 사용)
- 데이터: `assets/data/vocab.json`
- 이미지: `assets/images/*`

## 자주 쓰는 명령어
- 의존성 설치: `flutter pub get`
- 로컬 실행: `flutter run -d chrome`
- 웹 빌드: `flutter build web --base-href "/ItalianVocabApp/" --release`
- 배포: `main` 푸시 -> GitHub Actions -> GitHub Pages

## 작업 원칙
- 웹 우선(Web-only) 동작을 기준으로 기능 구현
- 대량 데이터/이미지 작업은 스크립트(`scripts/`) 중심으로 처리
- 배포 커밋에는 불필요 파일(`nul`, 임시 로그/캐시) 제외
- UI 텍스트는 한국어, 학습 데이터는 이탈리아어+한국어 의미/예문 조합 유지

## 주요 디렉토리
- `lib/`: 앱 코드 (화면, 위젯, 서비스)
- `assets/data/`: 단어 데이터(JSON)
- `assets/images/`: 단어 이미지
- `scripts/`: 데이터 가공/프롬프트 생성 자동화 스크립트
- `.github/workflows/`: CI/CD 파이프라인

## 오늘 진행 상태 (2026-02-15)
- 배치 프롬프트 파일 중심 데이터 제작 진행 (genspark_prompts_batch13.txt, genspark_prompts_batch14.txt, genspark_prompts_batch16.txt)
- genspark_prompts_batch14.txt에서 Image ID 805~854 구간 콘텐츠 정리/검토 진행
- 프롬프트 규칙(2x2 패널, 교육용 명확성, 숫자/번호 미표기) 준수 여부 점검
- 다음 작업: 중복 단어 항목 정리 및 품사/스토리 문장 자연스러움 최종 검수

## 현재 이슈 / TODO
- 워킹트리에 대량 untracked 파일이 있으므로 커밋 범위 선별 필요
- 일부 단어 데이터 품질(의미/예문 자연스러움) 추가 검수 필요
- 이미지 커버리지 및 파일명 규칙 일관성 점검 필요
- 상태 저장(학습 진도) 영속화 전략 재점검 필요

## 참고
- 라이브 URL: `https://titoliviomilazzo.github.io/ItalianVocabApp/`
- 최신 작업 이력은 `CHANGELOG.md` 기준으로 관리



