from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# 가상의 데이터베이스
USERS = [
    {"id": 1, "name": "Alice", "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "email": "bob@test.com"},
    {"id": 3, "name": "Charlie", "email": "charlie@gmail.com"},
    {"id": 4, "name": "David", "email": "david@fastapi.com"},
]


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "users": USERS})


@app.post("/search", response_class=HTMLResponse)
async def search(request: Request):
    form_data = await request.form()
    search_text = form_data.get("search", "").lower()

    # 검색어에 맞는 유저 필터링
    filtered_users = [
        u for u in USERS if search_text in u['name'].lower() or search_text in u['email'].lower()
    ]

    # 전체 페이지가 아닌 '유저 리스트 조각'만 반환
    return templates.TemplateResponse("user_list.html", {"request": request, "users": filtered_users})