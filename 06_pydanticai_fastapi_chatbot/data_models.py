from pydantic import BaseModel, Field
from pydantic_ai import ModelMessage

class ChatRequest(BaseModel):
    question: str = Field(description="users message or question to JokeBot")
    message_history: list[ModelMessage] = []

class ChatResponse(BaseModel):
    response: str = Field(description="Jokebots response with programming joke and emojis")
    message_history: list[ModelMessage]