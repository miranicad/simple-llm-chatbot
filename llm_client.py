from openai import OpenAI
from config import OPENAI_API_KEY, MODEL, MAX_TOKENS, TEMPERATURE

client = OpenAI(api_key=OPENAI_API_KEY)

def generate_response(messages):
    """
    Calls OpenAI API (streaming).

    :param messages: list of dicts:
        [{"role": "system"|"user"|"assistant", "content": "..."}]
    :return: generator/stream response
    """
    try:
        return client.chat.completions.create(
            model=MODEL,
            messages=messages,
            max_tokens=MAX_TOKENS,
            temperature=TEMPERATURE,
            stream=True,
        )
    except Exception as e:
        # Avoid printing secrets; this is okay as long as you don't log messages/keys
        print(f"Error beim API Call: {e}")
        raise
