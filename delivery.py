# delivery.py

import os
import requests
from secrets_check import check_required_env_vars

check_required_env_vars(["TELEGRAM_BOT_TOKEN", "TELEGRAM_CHAT_ID"])

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def send_report_via_telegram(filepath, caption="📄 Your LLM weekly report"):
    print("📤 Sending report via Telegram...")

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendDocument"

    try:
        with open(filepath, "rb") as doc:
            files = {"document": doc}
            data = {
                "chat_id": CHAT_ID,
                "caption": caption
            }
            response = requests.post(url, data=data, files=files)

        print(f"✅ Status: {response.status_code}")
        print("📨 Response:", response.json())

        if response.status_code != 200:
            raise Exception("Telegram API Error")

    except Exception as e:
        print(f"❌ Failed to send file: {e}")
