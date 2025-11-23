import joblib
import os
from app.config import settings

MODEL_PATH = settings.MODEL_PATH

class ModelLoader:
    _instance = None
    _model = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ModelLoader, cls).__new__(cls)
            cls._instance._load_model()
        return cls._instance

    def _load_model(self):
        if os.path.exists(MODEL_PATH):
            print(f"Loading model from {MODEL_PATH}...")
            self._model = joblib.load(MODEL_PATH)
        else:
            print(f"Model file not found at {MODEL_PATH}")
            self._model = None

    def get_model(self):
        return self._model

# Global instance
model_loader = ModelLoader()
