# region Gateway Schemas
from typing import Literal

from pydantic import BaseModel, Field


class MessageSchema(BaseModel):
    role: Literal["user", "assistant", "system"]
    content: str = Field(min_length=1, description="Message content cannot be empty")


class QueryRequest(BaseModel):
    query: str = Field(min_length=1, description="Query string cannot be empty")
    history: list[MessageSchema] = Field(
        default_factory=list, description="Chat history messages"
    )


class QueryResponse(BaseModel):
    response: str
    citations: list[str] = Field(default_factory=list)
    tool_calls_executed: list[str] = Field(default_factory=list)
    retrieved_documents: str | None = None


# endregion
