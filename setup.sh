python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
wget -P ./data/ https://blob.ngixx.me/processed_traffy_data_for_visualization.csv ./data/
python scripts/load_csv_to_sqlite.py
echo "
    Next Steps
    1) run all ai/train_model.ipynb
    2) run python run.py
"
