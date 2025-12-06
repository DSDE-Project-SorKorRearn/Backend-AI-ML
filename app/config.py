import os
import pandas as pd
from dotenv import load_dotenv


class Settings:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Settings, cls).__new__(cls)
            cls._instance._initialize()
        return cls._instance

    def load_csv(self):
        print("Loading CSV into RAM...")
        self.CLUSTER_DF = pd.read_csv("data/clustered_traffy.csv")
        print("Loaded!")

    def _initialize(self):
        load_dotenv()
        self.load_csv()
        self.DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./data/data.db")
        self.MODEL_PATH = os.getenv("MODEL_PATH", "app/ml/model.pkl")
        self.KMEANS_MODEL_PATH = os.getenv("KMEANS_MODEL_PATH", "ai/models/kmeans_model.pkl")
        self.SCALER_PATH = os.getenv("SCALER_PATH", "ai/models/scaler.pkl")
        self.CSV_PATH = os.getenv("CSV_PATH", "data/clean_traffy.csv")


settings = Settings()
