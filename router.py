# router.py

from utils.classifier import classify_task
from models.openai_handler import call_openai
from models.gemini_handler import call_gemini
from models.claude_handler import call_claude
from models.llama_handler import call_llama
from utils.evaluator import evaluate_response
from utils.cost_tracker import log_cost
from config import ROUTING_RULES

async def route_request(data):
    prompt = data.get("prompt", "")
    
    # Step 1: Classify task
    task_type = classify_task(prompt)  # e.g., "summarization", "code", "qna"
    
    # Step 2: Choose model based on routing rules
    model_choice = ROUTING_RULES.get(task_type, "openai")  # default fallback
    
    # Step 3: Route to the chosen model
    result = {"error": "Unknown model"}
    usage = {}
    
    if model_choice == "openai":
        result, usage = call_openai(prompt, task_type)
    elif model_choice == "gemini":
        result, usage = call_gemini(prompt, task_type)
    elif model_choice == "claude":
        result, usage = call_claude(prompt, task_type)
    elif model_choice == "llama":
        result, usage = call_llama(prompt, task_type)

    # Step 4: Evaluate and log
    score = evaluate_response(prompt, result.get("text", ""), task_type)
    log_cost(model_choice, usage, task_type, score)

    return {
        "response": result.get("text", ""),
        "model": model_choice,
        "task": task_type,
        "score": score,
        "usage": usage,
    }
