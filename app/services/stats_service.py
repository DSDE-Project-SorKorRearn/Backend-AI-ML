import json
import ast
from collections import Counter
from sqlalchemy import func
from sqlalchemy.orm import Session
from typing import Optional
from app.db.models import Traffy


def get_time_series_stats(db: Session):
    return (
        db.query(
            func.strftime("%Y", Traffy.timestamp).label("year"),
            func.strftime("%m", Traffy.timestamp).label("month"),
            func.count(Traffy.index).label("count"),
        )
        .filter(Traffy.timestamp != None)
        .group_by("year", "month")
        .all()
    )


def get_province_stats(db: Session):
    return (
        db.query(Traffy.province, func.count(Traffy.index).label("count"))
        .group_by(Traffy.province)
        .all()
    )


def get_district_stats(db: Session):
    return (
        db.query(Traffy.district, func.count(Traffy.index).label("count"))
        .group_by(Traffy.district)
        .all()
    )

def get_district_stats_by_name(db: Session, district_name: str):
    return (
        db.query(Traffy.district, func.count(Traffy.index).label("count"))
        .filter(Traffy.district == district_name)
        .group_by(Traffy.district)
        .first()
    )

def get_type_stats(db: Session):
    raw_results = db.query(Traffy.traffy_type).filter(Traffy.traffy_type != None).all()

    exploded = []

    for (type_str,) in raw_results:
        if not type_str:
            continue
        try:
            parsed = ast.literal_eval(type_str)
            if isinstance(parsed, list):
                exploded.extend(parsed)
            else:
                exploded.append(parsed)
        except:
            exploded.append(type_str)

    return dict(Counter(exploded))