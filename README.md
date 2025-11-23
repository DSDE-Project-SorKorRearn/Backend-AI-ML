#Backend AI ML for Sorkorrearn


## Structure

- `ai/`: Train AI code and load to ml
- `app/`: Main application code
  - `api/`: API endpoints
  - `db/`: Database models and connection
  - `ml/`: ML model loading and prediction
  - `schemas/`: Pydantic models
  - `services/`: Business logic
- `data/`: Data files (CSV, SQLite DB)
- `scripts/`: Utility scripts

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Load data:
   ```bash
   python scripts/load_csv_to_sqlite.py
   ```

3. Run server:
   ```bash
   uvicorn app.main:app --reload
   ```

4. Docs:
   - http://localhost:8000/docs
