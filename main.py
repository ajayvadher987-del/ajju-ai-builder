from fastapi import FastAPI
from pydantic import BaseModel

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
    return {
        "reply": f"You said: {request.message}"
    }
