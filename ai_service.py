import os
import requests


def ask_ai(message: str) -> str:
    api_key = os.getenv("AI_API_KEY")

    if not api_key:
        return "AI API key is not configured."

    model = os.getenv("AI_MODEL", "gemini-3.6-flash")

    url = (
        "https://generativelanguage.googleapis.com/"
        f"v1beta/models/{model}:generateContent"
    )

    headers = {
        "x-goog-api-key": api_key,
        "Content-Type": "application/json",
    }

    data = {
        "contents": [
            {
                "parts": [
                    {
                        "text": (
                            "You are Ajju AI Builder, a professional AI "
                            "assistant and coding agent. Give clear, useful "
                            "and accurate answers.\n\n"
                            f"User: {message}"
                        )
                    }
                ]
            }
        ]
    }

    try:
        response = requests.post(
            url,
            headers=headers,
            json=data,
            timeout=60
        )

        response.raise_for_status()
        result = response.json()

        return result["candidates"][0]["content"]["parts"][0]["text"]

    except requests.exceptions.RequestException as error:
        return f"AI connection error: {error}"

    except (KeyError, IndexError, TypeError):
        return "AI returned an unexpected response."
