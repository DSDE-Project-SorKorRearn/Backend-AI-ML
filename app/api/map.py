from typing import List, Optional

from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.schemas.map import MapPoint
from app.services import map_service

router = APIRouter(prefix="/map", tags=["Map"])


@router.get("/traffy",response_model=List[MapPoint])
def get_map_traffy(
    db: Session = Depends(get_db),
    type_name: Optional[str] = Query(None, description="Filter results by a specific Traffy type") 
):
    return map_service.get_map_data(db, type_name)