from rich import console
import requests
from app.core.config import settings

console = console.Console()

def parse_telegram_callback_request_data(message):
    chat_id = message.get("message", {}).get("chat", {}).get("id")
    text = message.get("message", {}).get("text")

    console.print(f"chat_id -> {chat_id}, text -> {text}")

    return chat_id, text


def send_message(chat_id, text="Hii from webhook side"):
    url = f'https://api.telegram.org/bot{settings.BOT_TOKEN}/sendMessage'
    payload = {
        "chat_id": chat_id,
        "text": text
    }

    print("url", url)
    r = requests.post(url, json=payload)
    if r.status_code != 200:
        raise Exception("Failed to fetch data from telegram")
    return r.json()
