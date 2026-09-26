import os
import requests


def ask_ai(message: str) -> str:
    api_key = os.getenv("AI_API_KEY")
    base_url = os.getenv("AI_BASE_URL")
    model = os.getenv("AI_MODEL")

    if not api_key:
        return "AI API key is not configured."

    if not base_url:
        return "AI base URL is not configured."

    if not model:
        return "AI model is not configured."

    try:
        response = requests.post(
            f"{base_url}/chat/completions",
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json",
            },
            json={
                "model": model,
                "messages": [
                    {
                        "role": "system",
                        "content": (
                            "You are Ajju AI Builder, a professional AI assistant "
                            "and coding agent. Give clear, useful and accurate answers."
                        ),
                    },
                    {
                        "role": "user",
                        "content": message,
                    },
                ],
                "temperature": 0.7,
            },
            timeout=60,
        )

        response.raise_for_status()
        data = response.json()

        return data["choices"][0]["message"]["content"]

    except requests.exceptions.RequestException as error:
        return f"AI connection error: {error}"

    except (KeyError, IndexError, TypeError):
        return "AI returned an unexpected response."
