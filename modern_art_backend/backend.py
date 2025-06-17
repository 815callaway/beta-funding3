from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Example predefined responses
questions_and_answers = {
    "Who is Picasso?": {"answer": "Picasso was a Spanish painter and sculptor.", "image": "https://example.com/picasso.jpg"},
    "What is Cubism?": {"answer": "Cubism is an early-20th-century art movement.", "image": "https://example.com/cubism.jpg"}
}

# Define request model
class Query(BaseModel):
    question: str

@app.post("/ask")
async def ask(query: Query):
    question = query.question
    # Find the response from predefined questions
    response = questions_and_answers.get(question, {"answer": "Sorry, I don't have an answer for that.", "image": None})
    return response
