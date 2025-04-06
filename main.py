
from fastapi import FastAPI
from pydantic import BaseModel
from sample_data import sample_assessments
from utils import embed_assessments, search_assessments

app = FastAPI()

class QueryInput(BaseModel):
    query: str

@app.post("/recommend")
def recommend(query_input: QueryInput):
    embeddings = embed_assessments(sample_assessments)
    results = search_assessments(query_input.query, sample_assessments, embeddings)
    return {"results": results}
