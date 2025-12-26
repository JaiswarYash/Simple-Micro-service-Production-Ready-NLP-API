from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.model import model_instance
from app.schemas import NlpRequest, NlpResponse
app = FastAPI(title="NLP Production API")

@asynccontextmanager
async def lifespan(app: FastAPI):
    # --- Startup ---
    print("Starting up: Loading ML model...")
    model_instance.load_model()
    yield

    # --- Shutdown ---
    print("Shutting down: Cleaning up resources...")
    # (Optional: Close database connections or clear GPU memory here)

app = FastAPI(title="NLP Production API", lifespan=lifespan)

@app.post("/predict", response_model=NlpResponse)
async def predict_sentiment(request: NlpRequest):
    raw_result = model_instance.predict(request.text)
    
    # The keys here MUST match NlpResponse fields exactly
    return {
        "text": request.text,           # Matches 'text'
        "sentiment": raw_result["label"], # Matches 'sentiment'
        "confidence": raw_result["score"] # Matches 'confidence'
    }