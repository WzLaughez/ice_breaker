import openai
from openai.error import AuthenticationError, RateLimitError

try:
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": "Hello!"}]
    )
    print(response['choices'][0]['message']['content'])
except AuthenticationError:
    print("Authentication error: Invalid or missing API key.")
except RateLimitError:
    print("Rate limit exceeded. Please try again later.")
except Exception as e:
    print(f"An error occurred: {e}")
