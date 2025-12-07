#Backend AI ML for Sorkorrearn


## Structure

- `ai/`: Train model clustering and load to csv
- `app/`: Main application code
  - `api/`: API endpoints
  - `db/`: Database models and connection
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

3. Run AI:
   - go to ai/
   - run all train_model.ipynb

4. Run server:
   ```bash
   python run.py
   ```

5. Docs:
   ```bash
   http://localhost:8000/docs
   ```
