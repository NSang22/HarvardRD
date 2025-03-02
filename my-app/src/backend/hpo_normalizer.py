# # hpo_normalizer.py
# from ontoma import OnToma

# ontoma = OnToma()

# def normalize_symptoms(symptom):
#     """Try to normalize a symptom to an HPO term."""
#     try:
#         result = ontoma.find_term(symptom)
#         return result["name"] if result else "Unknown Symptom"
#     except Exception:
#         return "Unknown Symptom"

# # Example
# if __name__ == "__main__":
#     print(normalize_symptoms("breath shortness"))  # Example usage
# # hpo_normalizer.py
# from ontoma import OnToma

# ontoma = OnToma()

# def normalize_symptoms(symptom):
#     """Try to normalize a symptom to an HPO term."""
#     try:
#         result = ontoma.find_term(symptom)
#         return result["name"] if result else "Unknown Symptom"
#     except Exception:
#         return "Unknown Symptom"

# # Example
# if __name__ == "__main__":
#     print(normalize_symptoms("breath shortness"))  # Example usage
import openai
import os
import requests
from groq import Groq
from dotenv import load_dotenv

load_dotenv() 

# Load API key securely
openai.api_key = os.getenv("OPENAI_API_KEY")  # Set this in your environment variables
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# def normalize_symptoms(symptom):
#     """Use Groq API to normalize a symptom to an HPO term."""
#     prompt = f"""
#     Given the user symptom description: '{symptom}', return the closest matching 
#     Human Phenotype Ontology (HPO) term. Only provide the term name and nothing else.
#     """

#     try:
#         response = client.chat.completions.create(
#             model="llama3-8b-8192",  # You can change this to another supported model
#             messages=[
#                 {"role": "system", "content": "You are an expert in medical terminology."},
#                 {"role": "user", "content": prompt}
#             ],
#             temperature=0.3
#         )

#         return response.choices[0].message.content.strip()  # Groq response format

#     except Exception as e:
#         print(f"Error: {e}")
#         return "Unknown Symptom"
    
# url = "http://127.0.0.1:8000/normalize"
# data = {
#     "symptom": "breath shortness"
# }

# response = requests.post(url, json=data)
# print(response.json())

def normalize_symptoms(symptoms):
    """Use Groq API to normalize a list of symptoms to HPO terms."""
    normalized_terms = {}
    for symptom in symptoms:
        prompt = f"Given the user symptom description: '{symptom}', return the closest matching Human Phenotype Ontology (HPO) term. Only provide the term name and nothing else."
        try:
            response = client.chat.completions.create(
                model="llama3-8b-8192",  # Or other supported models
                messages=[
                    {"role": "system", "content": "You are an expert in medical terminology."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.3
            )
            normalized_terms[symptom] = response.choices[0].message.content.strip()
        except Exception as e:
            print(f"Error: {e}")
            normalized_terms[symptom] = "Unknown Symptom"
    return normalized_terms

# Example usage
if __name__ == "__main__":
    print(normalize_symptoms("breath shortness"))
