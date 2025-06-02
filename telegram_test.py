import os
import requests
from dotenv import load_dotenv

load_dotenv(override=True)

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
data = {
    "chat_id": CHAT_ID,
    "text": "✅ Telegram bot is working! Your LLM Agent is ready to deliver reports."
}

response = requests.post(url, data=data)
print("Status:", response.status_code)
print("Response:", response.text)