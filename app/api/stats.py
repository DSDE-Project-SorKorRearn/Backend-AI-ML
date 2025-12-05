from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from typing import List, Optional, Dict
from app.db.database import get_db
from app.services import stats_service
from app.schemas.stats import TimeSeriesData, ProvinceData, DistrictData, TypeData

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

@router.get("/by-district/{district_name}", response_model=DistrictData)
def get_by_district_name(district_name: str, db: Session = Depends(get_db)):
    return stats_service.get_district_stats_by_name(db, district_name)

@router.get("/by-type", response_model=Dict[str,int])
def get_by_type(db: Session = Depends(get_db), type_name: Optional[str] = Query(None)):
    return stats_service.get_type_stats(db)