from fastapi import FastAPI
from pydantic import BaseModel
import google.generativeai as genai
import os
from dotenv import load_dotenv

#Carregar as veriaveis de ambiente
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

#Listar os modelos disponiveis
for m in genai.list_models():
    print(m.name)

MODEL_NAME = "gemini-3.8-flash"
app = FastAPI()

class PromptRequest(BaseModel):
    prompt: str

@app.post("/generate")
def generate_text(request: PromptRequest):
    try:
        model = genai.GenerativeModel(MODEL_NAME)
        response = model.generate_content(request.prompt)
        return {"response": response.text}
    except Exception as e:
        return {"error": str(e)}
