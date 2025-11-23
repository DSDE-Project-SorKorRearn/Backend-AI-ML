import os

from dotenv import load_dotenv


class Settings:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Settings, cls).__new__(cls)
            cls._instance._initialize()
        return cls._instance

    def _initialize(self):
        load_dotenv()
        self.DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./data/data.db")
        self.MODEL_PATH = os.getenv("MODEL_PATH", "app/ml/model.pkl")
        self.CSV_PATH = os.getenv("CSV_PATH", "data/clean_traffy.csv")


settings = Settings()
