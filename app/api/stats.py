from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.db.database import get_db
from app.services import stats_service
from app.schemas.stats import TimeSeriesData, ProvinceData, DistrictData

router = APIRouter(prefix="/stats", tags=["Stats"])

@router.get("/time-series", response_model=List[TimeSeriesData])
def get_time_series(db: Session = Depends(get_db)):
    return stats_service.get_time_series_stats(db)

@router.get("/by-province", response_model=List[ProvinceData])
def get_by_province(db: Session = Depends(get_db)):
    return stats_service.get_province_stats(db)

@router.get("/by-district", response_model=List[DistrictData])
def get_by_district(db: Session = Depends(get_db)):
    return stats_service.get_district_stats(db)
