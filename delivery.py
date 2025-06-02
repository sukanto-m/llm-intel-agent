# delivery.py

import os
import requests
from dotenv import load_dotenv

load_dotenv(override=True)

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def send_report_via_telegram(filepath, caption="📄 Your LLM weekly report"):
    if not BOT_TOKEN or not CHAT_ID:
        raise EnvironmentError("❌ Missing TELEGRAM_BOT_TOKEN or TELEGRAM_CHAT_ID in .env")

    print("📤 Sending report via Telegram...")
    print("🪪 BOT:", BOT_TOKEN[:10] + "...")  # Print first few characters only
    print("👤 CHAT ID:", CHAT_ID)

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
