from fastapi import FastAPI
from models import ChatRequest, ChatResponse
from agent import generate_response

app = FastAPI(title="SHL Assessment Recommender API")

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/chat", response_model=ChatResponse)
def chat_endpoint(request: ChatRequest):
    response = generate_response(request)
    return response

# To run: uvicorn main:app --reload
