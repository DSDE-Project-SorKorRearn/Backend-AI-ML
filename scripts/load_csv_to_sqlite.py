import os

import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()

# Adjust path to point to the DB file relative to where script is run
# Assuming script run from project root: python scripts/load_csv_to_sqlite.py
DB_URL = os.getenv("DATABASE_URL", "sqlite:///data/data.db")
CSV_PATH = os.getenv("CSV_PATH", "data/clean_traffy.csv")


def load_data():
    if not os.path.exists(CSV_PATH):
        print(f"File not found: {CSV_PATH}")
        return

    print(f"Reading {CSV_PATH}...")
    try:
        df = pd.read_csv(CSV_PATH)
    except Exception as e:
        print(f"Error reading CSV: {e}")
        return

    print("Processing data...")

    # Rename columns to match model
    df = df.rename(columns={"type": "traffy_type", "comment": "detail"})

    # Split coords into latitude and longitude
    if "coords" in df.columns:
        # coords format is usually "lat, long" or similar.
        # We'll assume "lat,long" string. Handle potential errors.
        def split_coords(coord_str):
            try:
                if pd.isna(coord_str):
                    return None, None
                parts = str(coord_str).split(",")
                if len(parts) >= 2:
                    return float(parts[0].strip()), float(parts[1].strip())
                return None, None
            except:
                return None, None

        coords = df["coords"].apply(split_coords)
        df["latitude"] = coords.apply(lambda x: x[1])
        df["longitude"] = coords.apply(lambda x: x[0])
        df = df.drop(columns=["coords"])

    # Convert timestamp and last_activity to datetime
    if "timestamp" in df.columns:
        df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")

    if "last_activity" in df.columns:
        df["last_activity"] = pd.to_datetime(df["last_activity"], errors="coerce")

    print("Connecting to database...")
    engine = create_engine(DB_URL)

    print("Writing to database...")
    # 'traffy' table name matches model definition
    # We use 'append' or 'replace'. 'replace' drops the table, which is good for full reload.
    # But we need to make sure the schema matches exactly what to_sql expects or let it create it.
    # Since we defined the model in SQLAlchemy, it's better to let to_sql create the table structure
    # if we are lazy, OR we should map columns carefully.
    # For this template, 'replace' is fine, but we should ensure columns match model.

    # Filter columns that exist in the dataframe and match the model (optional, but good practice)
    # For now, we assume the CSV + processing matches the model fields.

    df.to_sql("traffy", engine, if_exists="replace", index=True)

    print("Done!")


if __name__ == "__main__":
    load_data()
