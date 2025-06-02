# utils/fetch_papers.py

import requests
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone
import time

def fetch_llm_papers(max_results=10, days_back=7):
    query = 'all:"large language model" OR all:LLM'
    url = (
        f"http://export.arxiv.org/api/query?"
        f"search_query={query}&start=0&max_results={max_results}"
        f"&sortBy=submittedDate&sortOrder=descending"
    )

    headers = {
        "User-Agent": "Mozilla/5.0 (compatible; LLMIntelBot/1.0; +https://yourdomain.com)"
    }

    for attempt in range(3):
        try:
            print(f"🔍 Fetching arXiv papers (attempt {attempt + 1})...")
            response = requests.get(url, headers=headers, timeout=10)
            if response.status_code == 200:
                break
            else:
                print(f"⚠️ arXiv response: {response.status_code}")
        except Exception as e:
            print(f"⚠️ Request failed: {e}")
            time.sleep(2)
    else:
        print("❌ Failed to fetch arXiv data after 3 attempts.")
        return []

    # Parse Atom XML
    root = ET.fromstring(response.content)
    entries = root.findall("{http://www.w3.org/2005/Atom}entry")

    start_date = datetime.now(timezone.utc) - timedelta(days=days_back)
    papers = []

    for entry in entries:
        published_str = entry.find("{http://www.w3.org/2005/Atom}published").text.strip()
        published_dt = datetime.fromisoformat(published_str.replace("Z", "+00:00"))

        if published_dt >= start_date:
            paper = {
                "title": entry.find("{http://www.w3.org/2005/Atom}title").text.strip(),
                "summary": entry.find("{http://www.w3.org/2005/Atom}summary").text.strip(),
                "link": entry.find("{http://www.w3.org/2005/Atom}id").text.strip(),
                "published": published_str
            }
            papers.append(paper)

    print(f"📄 Total recent LLM papers found: {len(papers)}")
    return papers
