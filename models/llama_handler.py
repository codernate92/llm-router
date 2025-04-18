from llama_cpp import Llama
from config import LLAMA_MODEL_PATH

async def call_llama(prompt, task_type):
    try:
        # Initialize Llama model with context window and other parameters
        llm = Llama(
            model_path=LLAMA_MODEL_PATH,
            n_ctx=2048,  # Context window
            n_threads=4   # Number of CPU threads to use
        )
        
        # Generate response
        response = llm.create_completion(
            prompt=f"### User: {prompt}\n\n### Assistant:",
            max_tokens=1000,
            temperature=0.7,
            top_p=0.9,
            stop=["### User:", "\n\n"]
        )
        
        return {
            "text": response["choices"][0]["text"].strip(),
            "model": "llama-2"
        }, {
            "prompt_tokens": response["usage"]["prompt_tokens"],
            "completion_tokens": response["usage"]["completion_tokens"],
            "total_tokens": response["usage"]["total_tokens"]
        }
    except Exception as e:
        return {"text": f"Error: {str(e)}"}, {}