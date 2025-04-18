# utils/classifier.py

import re

def classify_task(prompt: str) -> str:
    """
    Simple rule-based task classifier.
    Returns one of: 'summarization', 'qna', 'code', or 'default'
    """
    prompt = prompt.lower().strip()

    # Simple regex and keyword checks
    if any(kw in prompt for kw in ["summarize", "tl;dr", "in summary"]):
        return "summarization"
    elif any(kw in prompt for kw in ["who", "what", "when", "where", "why", "how"]) and "?" in prompt:
        return "qna"
    elif "```" in prompt or any(kw in prompt for kw in ["write code", "generate code", "function", "algorithm"]):
        return "code"
    else:
        return "default"
