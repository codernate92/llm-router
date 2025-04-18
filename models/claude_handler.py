from anthropic import Anthropic
from config import ANTHROPIC_API_KEY

async def call_claude(prompt, task_type):
    client = Anthropic(api_key=ANTHROPIC_API_KEY)
    
    try:
        response = client.messages.create(
            model="claude-3-sonnet-20240229",
            max_tokens=1000,
            messages=[{"role": "user", "content": prompt}]
        )
        
        return {
            "text": response.content[0].text,
            "model": "claude-3"
        }, {
            "prompt_tokens": response.usage.input_tokens,
            "completion_tokens": response.usage.output_tokens
        }
    except Exception as e:
        return {"text": f"Error: {str(e)}"}, {}