# models/gemini_handler.py

import os
import requests

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent"

HEADERS = {
    "Content-Type": "application/json"
}


def call_gemini(prompt: str) -> str:
    payload = {
        "contents": [
            {
                "parts": [
                    {"text": prompt}
                ]
            }
        ]
    }

    try:
        response = requests.post(
            f"{GEMINI_API_URL}?key={GEMINI_API_KEY}",
            headers=HEADERS,
            json=payload
        )

        if response.status_code == 400:
            raise Exception("Bad request: The prompt may be invalid")
        elif response.status_code == 401:
            raise Exception("Authentication failed: Check your API key")
        elif response.status_code != 200:
            raise Exception(f"API error {response.status_code}: {response.text}")

        result = response.json()
        
        # Safely navigate the response structure
        candidates = result.get("candidates", [])
        if not candidates:
            return "No response generated"
            
        content = candidates[0].get("content", {})
        parts = content.get("parts", [])
        if not parts:
            return "Empty response received"
            
        return parts[0].get("text", "No text in response")

    except requests.exceptions.RequestException as e:
        raise Exception(f"Network error: {str(e)}")
    except ValueError as e:
        raise Exception(f"Invalid JSON response: {str(e)}")
