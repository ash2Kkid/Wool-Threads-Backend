import os
import requests

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

BASE_URL = "https://openrouter.ai/api/v1/chat/completions"


def call_openrouter(messages, max_tokens=120):

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
    }

    payload = {
        "model": "openai/gpt-4o-mini",
        "messages": messages,
        "max_tokens": max_tokens,
        "temperature": 0.3,
    }

    res = requests.post(BASE_URL, headers=headers, json=payload)

    if res.status_code != 200:
        raise Exception(res.text)

    return res.json()["choices"][0]["message"]["content"]