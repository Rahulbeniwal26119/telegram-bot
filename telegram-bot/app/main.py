from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from app.telegram_helper import parse_telegram_callback_request_data, send_message

from app.core.config import settings


def get_application():
    _app = FastAPI(title=settings.PROJECT_NAME)

    _app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return _app


app = get_application()


@app.get("/")
@app.post("/")
async def index(request: Request):
    try:
        req_info = await request.json()
        id, text = parse_telegram_callback_request_data(req_info)
        print(id, text)

        if text == "Hii":
            res = send_message(id, "Hello")
        else:
            res = send_message(id)
        print(res)
    except Exception as e:
        print(e)
    return {
        "a" : "Hii World"
    }
