from sqlalchemy.orm import Session

from app.db.models import Traffy


def get_map_data(db: Session):
    return db.query(
        Traffy.ticket_id, Traffy.latitude, Traffy.longitude, Traffy.traffy_type
    ).all()
