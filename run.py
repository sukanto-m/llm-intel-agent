# run.py

import json
from pathlib import Path
from datetime import datetime
from commander import run_mission
from delivery import send_report_via_telegram

def save_report(result):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    report_path = Path(f"llm_weekly_report_{timestamp}.txt")

    with open(report_path, "w") as f:
        f.write("🧠 Summaries + Code Demos:\n")
        f.write(result["summaries"] + "\n\n")
        f.write("📚 Citations:\n")
        for citation in result["citations"].get("citations", []):
            f.write(f"- {citation}\n")

    return report_path

if __name__ == "__main__":
    result = run_mission()

    if "error" in result:
        print(f"❌ Mission failed: {result['error']}")
    else:
        # Save report
        report_path = save_report(result)

        print(f"\n✅ Report saved to: {report_path}\n")
        print("🧠 Summaries + Code Demos:\n")
        print(result["summaries"])
        print("\n📚 Citations:\n")
        for citation in result["citations"].get("citations", []):
            print(f"- {citation}")

        # Send via Telegram
        send_report_via_telegram(report_path)
