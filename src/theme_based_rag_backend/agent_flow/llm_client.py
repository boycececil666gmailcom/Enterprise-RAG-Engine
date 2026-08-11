#region Imports & AI Models Initialization
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from src.theme_based_rag_backend.config import (
    GEMINI_API_KEY,
    GEMINI_MODEL,
    GEMINI_TEMPERATURE,
    GEMINI_EMBED_MODEL
)

api_key = GEMINI_API_KEY if (GEMINI_API_KEY and GEMINI_API_KEY.strip()) else "dummy_key_for_testing"

# Primary LLM instance for chat response generation
llm = ChatGoogleGenerativeAI(
    model=GEMINI_MODEL,
    google_api_key=api_key,
    temperature=GEMINI_TEMPERATURE
)

# Shared Embeddings instance for vector search and query classification
embeddings = GoogleGenerativeAIEmbeddings(
    model=GEMINI_EMBED_MODEL,
    google_api_key=api_key
)
#endregion
