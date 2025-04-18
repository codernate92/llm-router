import os
from dotenv import load_dotenv

load_dotenv()

ROUTING_RULES = {
    "summarization": "openai",
    "code": "claude",
    "qna": "gemini",
    "creative": "llama"
}

# API Keys
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
LLAMA_MODEL_PATH = os.getenv("LLAMA_MODEL_PATH", "path/to/llama/model.gguf")
