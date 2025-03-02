# from fastapi import FastAPI
# import openai, os
# from pydantic import BaseModel
# from hpo_normalizer import normalize_symptoms  # Import function

# app = FastAPI()

# class SymptomRequest(BaseModel):
#     symptom: str


# @app.post("/normalize")
# async def normalize_symptoms(data: SymptomRequest):
#     """Use OpenAI API to normalize a symptom to an HPO term."""
#     prompt = f"Given the user symptom description: '{request.symptom}', return the closest matching Human Phenotype Ontology (HPO) term. Only provide the term name and nothing else."

#     try:
#         response = openai.ChatCompletion.create(
#             model="gpt-3.5-turbo",
#             messages=[
#                 {"role": "system", "content": "You are an expert in medical terminology."},
#                 {"role": "user", "content": prompt}
#             ],
#             temperature=0.3
#         )

#         return {"input_symptom": request.symptom, "normalized_hpo_term": response["choices"][0]["message"]["content"].strip()}

#     except Exception as e:
#         return {"input_symptom": request.symptom, "normalized_hpo_term": "Unknown Symptom", "error": str(e)}

# # @app.get("/")
# # def read_root():
# #     return {"message": "Hello World"}

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)
# # To run the server, use the command:
# # uvicorn app:app --reload  
from fastapi import FastAPI
from pydantic import BaseModel
from hpo_normalizer import normalize_symptoms 
import uvicorn # Import function from your updated script

app = FastAPI()

class SymptomRequest(BaseModel):
    symptoms: list[str]

# @app.post("/normalize")
# async def normalize_symptom_endpoint(data: SymptomRequest):
#     """API endpoint to normalize a symptom to an HPO term using Groq API."""
#     try:
#         hpo_term = normalize_symptoms(data.symptom)
#         return {"input_symptom": data.symptom, "normalized_hpo_term": hpo_term}
    
#     except Exception as e:
#         return {"input_symptom": data.symptom, "normalized_hpo_term": "Unknown Symptom", "error": str(e)}
@app.post("/normalize")
async def normalize_symptom_endpoint(data: SymptomRequest):
    """API endpoint to normalize a list of symptoms to HPO terms using Groq API."""
    try:
        hpo_terms = normalize_symptoms(data.symptoms)
        return {"input_symptoms": data.symptoms, "normalized_hpo_terms": hpo_terms}
    
    except Exception as e:
        return {"input_symptoms": data.symptoms, "normalized_hpo_terms": "Unknown Symptom", "error": str(e)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)
