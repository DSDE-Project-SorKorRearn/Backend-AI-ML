from sqlalchemy.orm import Session
from sqlalchemy import func

from app.db.models import Traffy


def get_map_data(db: Session):
    results = db.query(
        Traffy.latitude,
        Traffy.longitude
    ).all()
    return [
        {"latitude": r[0], "longitude": r[1]} 
        for r in results
    ]
