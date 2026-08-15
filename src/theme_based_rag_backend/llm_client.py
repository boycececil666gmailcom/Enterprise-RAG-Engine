#region LLM Clients
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings

from .config import GEMINI_API_KEY, GEMINI_EMBED_MODEL, GEMINI_MODEL, GEMINI_TEMPERATURE

# Primary LLM instance for standard generation
llm = ChatGoogleGenerativeAI(
    model=GEMINI_MODEL,
    google_api_key=GEMINI_API_KEY,
    temperature=GEMINI_TEMPERATURE,
)

# LLM instance configured with lower temperature for HyDE passage generation
hyde_llm = ChatGoogleGenerativeAI(
    model=GEMINI_MODEL,
    google_api_key=GEMINI_API_KEY,
    temperature=0.3,
)

# Shared embeddings client for vector store and theme similarity
embeddings = GoogleGenerativeAIEmbeddings(
    model=GEMINI_EMBED_MODEL,
    google_api_key=GEMINI_API_KEY,
)
#endregion
