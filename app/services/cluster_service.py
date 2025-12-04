import pandas as pd
from sqlalchemy import func
from sqlalchemy.orm import Session

from app.db.models import Traffy
from app.ml.clustering import predict_cluster


def get_cluster_data(db: Session):
    # Query data for clustering
    query = db.query(
        Traffy.province, Traffy.district, func.count(Traffy.index).label("count")
    ).group_by(Traffy.province, Traffy.district)
    df = pd.read_sql(query.statement, db.bind)

    if df.empty:
        return []

    # Predict clusters
    # Assuming model expects 'count' or other features.
    # For this template, we pass the whole DF.
    df["cluster_id"] = predict_cluster(df[["count"]])

    return df.to_dict(orient="records")
