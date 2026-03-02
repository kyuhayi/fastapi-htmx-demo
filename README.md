# FastAPI + htmx Real-time Search Demo

이 프로젝트는 현대적인 Python 도구인 **uv**와 **mise**를 활용하여, JavaScript 프레임워크 없이 **FastAPI**와 **htmx**만으로 구현한 실시간 인터렉티브 웹 데모입니다.



## 🛠 Tech Stack

* **Backend:** [FastAPI](https://fastapi.tiangolo.com/) (Python 3.12+)
* **Frontend:** [htmx](https://htmx.org/) (No JavaScript written)
* **Template Engine:** Jinja2
* **Package Manager:** [uv](https://github.com/astral-sh/uv) (Fast & Modern)
* **Tool Manager:** [mise](https://mise.jdx.dev/) (Tool version management)

## 🚀 Key Features

* **Search-as-you-type:** 사용자가 입력을 멈추면(300ms delay) 자동으로 서버에 요청을 보내 리스트를 필터링합니다.
* **Partial HTML Swap:** JSON API 대신 서버에서 렌더링된 HTML 조각을 전송하여 클라이언트 사이드 로직을 최소화합니다.
* **Modern Workflow:** `uv`를 통해 초고속 패키지 설치 및 의존성 관리를 수행합니다.

## 📋 Prerequisites

이 프로젝트는 환경 관리를 위해 `mise`와 `uv` 사용을 권장합니다.

```zsh
# mise가 설치되어 있다면 도구 자동 설치
mise install

Installation & Running
저장소 클론:

Bash
git clone [https://github.com/kyuhayi/fastapi-htmx-demo.git](https://github.com/kyuhayi/fastapi-htmx-demo.git)
cd fastapi-htmx-demo
의존성 설치 (uv 사용):

Bash
uv sync
서버 실행:

Bash
uv run uvicorn main:app --reload
접속:
브라우저에서 http://127.0.0.1:8000 접속

.
├── main.py              # FastAPI 서버 로직 및 라우팅
├── templates/           # Jinja2 템플릿 폴더
│   ├── index.html       # 메인 레이아웃 및 htmx 설정
│   └── user_list.html   # 업데이트되는 HTML 조각 (Partial)
├── pyproject.toml       # uv 프로젝트 설정 및 의존성
├── uv.lock              # 의존성 잠금 파일
└── .mise.toml           # mise 도구 버전 설정