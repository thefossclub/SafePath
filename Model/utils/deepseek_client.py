# Model/utils/deepseek_client.py
import os
import requests
import json

DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY", "")
DEEPSEEK_URL = "https://api.deepseek.com/v1/chat/completions"

def rate_segment_risk(segment_summary):
    """
    Takes a crime summary dict and returns a risk value between 0 and 1.
    """
    # Safety: If no API key, return fallback so the service still works
    if not DEEPSEEK_API_KEY:
        return 0.2  # default fallback

    prompt = f"""
You score how dangerous a street segment is.

Crime summary (near this road):
{segment_summary}

Return ONLY a float in [0,1] measuring risk.
Example:
0.23
"""

    payload = {
        "model": "deepseek-chat",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.2,
    }

    response = requests.post(
        DEEPSEEK_URL,
        json=payload,
        headers={
            "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
            "Content-Type": "application/json",
        },
    )
    try:
        txt = response.json()["choices"][0]["message"]["content"].strip()
        return float(txt)
    except Exception:
        return 0.2

