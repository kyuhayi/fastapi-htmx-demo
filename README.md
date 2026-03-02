# FastAPI + htmx Real-time Search Demo

이 프로젝트는 **FastAPI**와 **htmx**를 결합하여 JavaScript 프레임워크 없이 실시간 검색 기능을 구현한 데모입니다.

## 주요 기능
- **Search-as-you-type**: 타이핑 시 실시간 필터링 (300ms 딜레이)
- **Partial Updates**: 페이지 전체가 아닌 HTML 조각만 교체
- **No JS**: 순수 HTML 속성만으로 인터렉티브 UI 구현

## 실행 방법
1. 패키지 설치: `pip install fastapi uvicorn jinja2 python-multipart`
2. 서버 실행: `uvicorn main:app --reload`
3. 접속: `http://127.0.0.1:8000`