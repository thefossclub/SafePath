# safepath/utils/deepseek_client.py
import requests, json

DEEPSEEK_API_KEY = "YOUR_KEY"
DEEPSEEK_URL = "https://api.deepseek.com/v1/chat/completions"

def rate_segment_risk(segment_summary):
    """
    Input: dict with crime counts near segment
    Output: risk value 0–1
    """

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
        "messages": [{"role":"user", "content":prompt}],
        "temperature": 0.2
    }

    r = requests.post(DEEPSEEK_URL, json=payload, headers={
        "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
        "Content-Type": "application/json"
    })

   txt = r.json()["choices"][0]["message"]["content"].strip()
    try:
        return float(txt.strip())
    except:
        return 0.2   # fallback

