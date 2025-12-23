from fastapi import FastAPI
from pydantic import BaseModel
import requests
import os
import uvicorn

app = FastAPI()


GEMINI_API_KEY = "AIzaSyAK4gprY04BltMbfknoFipwb9EX58Ad17M"
GEMINI_API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"


class TranslationRequest(BaseModel):
    text: str
    source_lang: str
    target_lang: str


@app.post("/translate")
def translate_text(request: TranslationRequest):
    headers = {"Content-Type": "application/json"}
    params = {"key": GEMINI_API_KEY}

    prompt = (
        f"Translate the following text from {request.source_lang} to {request.target_lang}:\n\n"
        f"{request.text}"
    )

    payload = {"contents": [{"parts": [{"text": prompt}]}]}

    response = requests.post(GEMINI_API_URL, headers=headers, params=params, json=payload)

    if response.status_code != 200:
        return {"error": response.text}

    data = response.json()
    translated_text = (
        data.get("candidates", [{}])[0]
        .get("content", {})
        .get("parts", [{}])[0]
        .get("text", "")
    )

    return {"translated_text": translated_text}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
