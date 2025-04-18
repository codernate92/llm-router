from openai import AsyncOpenAI
from config import OPENAI_API_KEY

async def call_openai(prompt, task_type):
    client = AsyncOpenAI(api_key=OPENAI_API_KEY)
    
    try:
        response = await client.chat.completions.create(
            model="gpt-4-turbo-preview",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=1000
        )
        
        return {
            "text": response.choices[0].message.content,
            "model": "gpt-4"
        }, {
            "prompt_tokens": response.usage.prompt_tokens,
            "completion_tokens": response.usage.completion_tokens,
            "total_tokens": response.usage.total_tokens
        }
    except Exception as e:
        return {"text": f"Error: {str(e)}"}, {}