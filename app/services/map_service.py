from sqlalchemy.orm import Session
from sqlalchemy import func

from app.db.models import Traffy


def get_map_data(db: Session):
    results = db.query(
        Traffy.index,    
        Traffy.latitude,   
        Traffy.longitude,    
        Traffy.traffy_type   
    ).limit(100).all()
    return [
        {"index": r[0], "latitude": r[1], "longitude": r[2], "traffy_type": r[3]} 
        for r in results
    ]
