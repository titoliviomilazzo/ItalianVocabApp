```markdown
# 프로젝트: Italiano 2000 - 이탈리아어 플래쉬카드 앱 개발 마스터 플랜

## 1. 개발 환경 및 도구 (Tech Stack)
* **IDE:** Google Antigravity (Mission Control 에이전트 활용)
* **프레임워크:** Flutter (Cross-platform)
* **데이터 관리:** 로컬 JSON (`assets/data/vocab.json`)
* **에셋 생성:** Genspark Pro (이미지), Python (데이터 전처리)
* **모델:** Gemini 1.5 Pro (via Antigravity)

## 2. 단계별 실행 가이드 (Antigravity 에이전트 지시용)

### 1단계: 데이터 스키마 및 인프라 구축
Antigravity 에이전트에게 다음 프롬프트를 입력하여 프로젝트를 시작합니다.
> "Flutter 프로젝트를 생성하고 다음 JSON 구조를 지원하는 데이터 모델을 작성해줘. 2,000개의 단어를 로컬에서 로드할 수 있어야 해.
> 스키마: { 'id': int, 'word': string, 'gender': string, 'level': string, 'meaning': string, 'pronunciation': string, 'image_path': string }"

### 2단계: 데이터 자동 생성 (Batch Harvesting)
Antigravity 에이전트에게 2,000개 리스트 생성을 자동화하도록 명령합니다. (토큰 제한을 고려하여 200개 단위 배치를 지시)
> "이탈리아어 A1.2부터 B2.2까지, 그리고 일상 회화 빈도가 높은 단어 200개를 먼저 추출해줘. 
> 1. B레벨 비중을 60%로 설정할 것. 
> 2. 명사는 (m.), (f.) 성별을 포함할 것. 
> 3. 결과는 `vocab_part1.json`으로 저장해줘. 이 과정을 총 10회 반복하여 2,000개를 채울 거야."

### 3단계: Genspark Pro 에셋 생성 및 매칭
Genspark Pro를 통해 생성된 이미지를 파이썬으로 관리합니다.
* **Genspark 지시:** "이탈리아어 단어 리스트에 대해 'Minimalist 3D Illustration style'로 이미지를 생성해줘."
* **Python 스크립트 역할:** 다운로드된 이미지 파일명을 `word_id.webp`로 일괄 변경하고 JSON의 `image_path`와 동기화.

### 4단계: UI/UX 구현 (Vibe Coding)
Antigravity 에이전트에게 기능 구현을 요청합니다.
* **기능 1:** 화면 중앙 플래쉬카드 위젯 (애니메이션 포함).
* **기능 2:** 터치 시 카드 뒤집기 (앞: 이탈리아어+이미지+발음, 뒤: 한국어).
* **기능 3:** 수준별(A1.2 ~ B2.2) 필터링 시스템.
* **기능 4:** 로컬 이미지 로딩 최적화 및 캐싱.

## 3. 구조적 고려사항 및 리스크 관리

### 이미지 및 용량 최적화
* **해결책:** 모든 이미지는 512x512 해상도의 WebP 포맷으로 변환. 2,000장 기준 약 150~200MB 수준으로 앱 용량 제어.
* **데이터 정합성:** Antigravity 에이전트가 단어 중복을 체크하도록 `Set` 자료구조를 사용하여 검증 지시.

### Human-AI 역할 분담
* **Antigravity:** Flutter 코드 작성, JSON 파싱 logic, UI 레이아웃.
* **Marcus (User):** Python을 이용한 파일명 일괄 정리, Genspark 이미지 다운로드 관리, 최종 빌드 및 기기(SM6 RE 연동 등 모바일 환경) 테스트.

## 4. Antigravity 미션 컨트롤 초기 프롬프트 (복사해서 사용)
```text
Role: 전문 Flutter 개발자 에이전트
Task: 이탈리아어 2000 단어 플래쉬카드 앱 개발
Constraints:
- UI 디자인은 최소화하되 작동에 집중할 것.
- 모든 데이터는 assets 내의 JSON과 WebP 이미지를 사용할 것.
- B1, B2 레벨 단어 비중을 높게 유지할 것.
- 단계별로 파일을 생성하고 나에게 확인을 받을 것.

```

```

```