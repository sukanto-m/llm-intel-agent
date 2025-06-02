# delivery.py

import os
import requests

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def send_report_via_telegram(report_path):
    if not BOT_TOKEN or not CHAT_ID:
        print("❌ Missing TELEGRAM_BOT_TOKEN or TELEGRAM_CHAT_ID.")
        return

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendDocument"
    caption = "📄 Weekly LLM Intelligence Report"

    try:
        with open(report_path, "rb") as f:
            files = {"document": f}
            data = {"chat_id": CHAT_ID, "caption": caption}

            response = requests.post(url, data=data, files=files)

            print("📨 Telegram API status:", response.status_code)
            print("📨 Telegram API response:", response.text)

            if response.ok:
                print("✅ Report successfully sent via Telegram.")
            else:
                print("❌ Telegram delivery failed.")
    except Exception as e:
        print(f"❌ Exception during Telegram delivery: {e}")