# main.py

from fastapi import FastAPI
from router import router

app = FastAPI(
    title="LLM Smart Router 🔀",
    description="A GenAI-powered API that intelligently routes prompts to OpenAI or Gemini based on task type.",
    version="1.0.0"
)

# Attach the router
app.include_router(router)

# Optional root route
@app.get("/")
async def root():
    return {"message": "LLM Router is alive 🚀"}
