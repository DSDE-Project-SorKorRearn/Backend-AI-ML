from sqlalchemy import func
from sqlalchemy.orm import Session

from app.db.models import Traffy


def get_time_series_stats(db: Session):
    return (
        db.query(
            func.strftime("%Y", Traffy.timestamp).label("year"),
            func.strftime("%m", Traffy.timestamp).label("month"),
            func.count(Traffy.id).label("count"),
        )
        .group_by("year", "month")
        .all()
    )


def get_province_stats(db: Session):
    return (
        db.query(Traffy.province, func.count(Traffy.ticket_id).label("count"))
        .group_by(Traffy.province)
        .all()
    )


def get_district_stats(db: Session):
    return (
        db.query(Traffy.district, func.count(Traffy.ticket_id).label("count"))
        .group_by(Traffy.district)
        .all()
    )
