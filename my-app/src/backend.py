import openai
from dotenv import load_dotenv
import os
openai_api_key = os.getenv("OPENAI_API_KEY")

# Set the OpenAI API key
openai.api_key = openai_api_key

# Example function to make an API call to OpenAI
def get_openai_response(prompt):
    response = openai.Completion.create(
        engine="davinci-codex",
        prompt=prompt,
        max_tokens=100
    )
    return response.choices[0].text.strip()

# Example usage
if __name__ == "__main__":
    prompt = "Translate the following English text to French: 'Hello, how are you?'"
    response = get_openai_response(prompt)
    print(response)