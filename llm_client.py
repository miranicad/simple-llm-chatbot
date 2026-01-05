from openai import  OpenAI
from config import OPENAI_API_KEY, MODEL, MAX_TOKENS, TEMPERATURE

client = OpenAI(api_key=OPENAI_API_KEY)

def generate_response(messages):

    """
    Calls OpenAI API

    :param messages: List messages in format:
                    [{"role": "user", "content": "Hallo"}]
    :return:
        Generator for response
    """

    try:
        response = client.chat.completions.create(
            messages= messages,
            model= MODEL,
            max_tokens=MAX_TOKENS,
            temperature = TEMPERATURE, # prediction for next word
            stream = True # answer is shown step by step
        )

        return response

    except Exception as e:
        print(f"Error beim API Call: {e}")
        raise