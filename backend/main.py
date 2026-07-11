from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="TalentLens AI API", version="0.1.0")

class AnalysisRequest(BaseModel):
    repo_url: str
    job_description: str

@app.get("/")
def read_root():
    return {"message": "Welcome to TalentLens AI Backend - Week 1 Foundation"}

@app.post("/api/analyze")
async def analyze_repository(request: AnalysisRequest):
    if not request.repo_url or not request.job_description:
        return {"error": "Missing required fields"}
        
    return {
        "status": "success",
        "message": "Repository analysis pipeline initiated for Week 1 MVP."
    }
