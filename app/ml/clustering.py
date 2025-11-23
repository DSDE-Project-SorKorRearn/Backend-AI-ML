import pandas as pd
from .model_loader import model_loader

def predict_cluster(df: pd.DataFrame):
    model = model_loader.get_model()
    if model is None:
        # Fallback if model not found
        return [0] * len(df)
    return model.predict(df)
