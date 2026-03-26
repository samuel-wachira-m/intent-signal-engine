from fastapi import FastAPI
from fastapi.responses import JSONResponse
import logging
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI(
    title="Intent Signal Engine",
    description="AI-powered Reddit lead detection for B2B SaaS",
    version="1.0.0"
)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.get("/")
def read_root():
    return {"message": "Intent Signal Engine API is running"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.post("/api/classify")
def classify_intent(text: str):
    """Classify text for buying intent signals"""
    logger.info(f"Classifying text: {text[:50]}...")
    return {"intent": "pending", "confidence": 0.0}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)