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


# Load API key securely
openai.api_key = os.getenv("OPENAI_API_KEY")  # Set this in your environment variables

def normalize_symptoms(symptom):
    """Use OpenAI API to normalize a symptom to an HPO term."""
    prompt = f"""
    Given the user symptom description: '{symptom}', return the closest matching 
    Human Phenotype Ontology (HPO) term. Only provide the term name and nothing else.
    """

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Use "gpt-3.5-turbo" if you want a cheaper option
            messages=[{"role": "system", "content": "You are an expert in medical terminology."},
                      {"role": "user", "content": prompt}],
            temperature=0.3  # Lower temperature for consistency
        )

        return response["choices"][0]["message"]["content"].strip()

    except Exception as e:
        print(f"Error: {e}")
        return "Unknown Symptom"
    
url = "http://127.0.0.1:8000/normalize"
data = {
    "symptom": "breath shortness"
}

response = requests.post(url, json=data)
print(response.json())

# Example usage
if __name__ == "__main__":
    print(normalize_symptoms("breath shortness"))  # Should return "Dyspnea"
