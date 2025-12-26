import torch
from transformers import pipeline
from app.core.config import app_config

class SentimentModel:
    def __init__(self):
        self.pipeline = None
    
    def load_model(self):
        if self.pipeline is None:
            print(f"-----Loading model: {app_config.model_name}----------")

            device = 0 if torch.cuda.is_available() else -1

            self.pipeline = pipeline(
            "sentiment-analysis",
            model=app_config.model_name,
            device=device,
            #clean_up_tokenization_spaces=True  # Add this to remove the warning
            )
            
            print("Model loaded successfully.")
    
    def predict(self, text: str):
        if self.pipeline is None:
            raise ValueError("Model is not loaded. Call load_model() before prediction.")
        
        results = self.pipeline(text)[0]
        return results

model_instance = SentimentModel()
    
