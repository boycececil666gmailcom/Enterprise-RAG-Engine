#region Imports & AI Models Initialization
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from src.theme_based_rag_backend.config import (
    GEMINI_API_KEY,
    GEMINI_MODEL,
    GEMINI_TEMPERATURE,
    GEMINI_EMBED_MODEL
)


# Primary LLM instance for standard chat response generation
llm = ChatGoogleGenerativeAI(
    model=GEMINI_MODEL,
    google_api_key=GEMINI_API_KEY,
    temperature=GEMINI_TEMPERATURE
)

# Dedicated LLM instance with lower temperature for creative HyDE hypothetical document generation
hyde_llm = ChatGoogleGenerativeAI(
    model=GEMINI_MODEL,
    google_api_key=GEMINI_API_KEY,
    temperature=0.3
)

# Shared Embeddings instance for vector search and query classification
embeddings = GoogleGenerativeAIEmbeddings(
    model=GEMINI_EMBED_MODEL,
    google_api_key=GEMINI_API_KEY
)
#endregion
