# from openai import OpenAI
# import os
# from dotenv import load_dotenv

# load_dotenv() 

# client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))  # Initialize client

# response = client.chat.completions.create(
#     model="gpt-4o-mini",
#     messages=[
#         {"role": "system", "content": "You are a medical terminology expert."},
#         {"role": "user", "content": "What is dyspnea?"}
#     ],
#     temperature=0.3
# )

# print(response.choices[0].message.content.strip())  # Extract response

from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv() 


client = Groq(api_key=os.getenv("GROQ_API_KEY"))

response = client.chat.completions.create(
    model="llama3-8b-8192",  # Or other supported models
    messages=[{"role": "user", "content": "Shortness of breath is most closely related to what medical term?"}]
)

print(response.choices[0].message.content)