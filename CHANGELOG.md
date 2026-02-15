# Changelog

## 2026-02-15

### 진행상태 업데이트 (오전)
- ItalianVocabApp 프롬프트 배치 작업 진행 (genspark_prompts_batch13.txt, genspark_prompts_batch14.txt, genspark_prompts_batch16.txt)
- 배치14 기준 Image ID 805~854 구간(단어 biglietteria ~ bomba) 스토리/패널 문구 정리
- 프롬프트 공통 규칙 유지 확인: 4패널 그리드, 품사 표기 타이틀 배너, 패널 내 숫자/번호 미표기
- 중복/품질 점검 포인트 정리: 중복 단어 항목(예: blocco) 및 문장 자연스러움 후속 검수 필요
### Deploy / 데이터 반영
- 배포 커밋 정리: `Deploy: Update images and data (excluding nul)`
- 이미지/데이터 최신 변경분 반영 및 배포 파이프라인 점검
- 불필요 파일(`nul`) 제외 기준 명시

### 작업 상태
- 대량 이미지 및 데이터 추가 작업이 로컬 워킹트리에 남아 있음
- 배포 전 변경 범위를 선별해 커밋하는 운영 방식 유지

## 2026-02-13

### 데이터/브랜딩 확장
- 신규 이미지 추가
- 커스텀 앱 아이콘 적용
- B1/B2 어휘 데이터 추가 (`B1-voca-enriched.csv`, `B2-voca-copy-final.csv`)
- 문서 정리: `CLAUDE.md`, `CHANGELOG.md` 갱신

## 2026-02-12

### 기능 고도화
- TTS 적용/조정 (Web 환경 기준)
- 예문 추가 및 플래시카드 뒷면 구성 단순화
- 260+ 어휘 이미지 반영 및 단어 데이터 업데이트

### CI/CD 안정화
- Flutter 버전/웹 빌드 설정 조정
- GitHub Pages 배포 경로(base href) 및 워크플로우 수정
- PWA/iOS 메타 태그 및 브랜딩 반영

### 리브랜딩
- 앱 아이덴티티를 `Dammi Parole` 방향으로 정비
- UI 테마/톤 정리

## 2026-02-11

### 핵심 학습 기능 구현
- 검색, 통계, 카드 애니메이션 개선
- 학습 모드(플래시카드/퀴즈) 주요 흐름 구현
- README 업데이트 (기능, 구조, 배포 정보)

## 2026-02-10

### 프로젝트 시작
- 초기 프로젝트 구조 및 기본 UI 구성
- 초기 데이터/문서 베이스 구축



