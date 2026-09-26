from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv

from ai_service import ask_ai

load_dotenv()

app = FastAPI(title="Ajju AI Builder")


class ChatRequest(BaseModel):
    message: str


@app.get("/")
def home():
    return {
        "status": "online",
        "app": "Ajju AI Builder",
        "version": "1.0"
    }


@app.post("/chat")
def chat(request: ChatRequest):
    reply = ask_ai(request.message)

    return {
        "reply": reply
    }
