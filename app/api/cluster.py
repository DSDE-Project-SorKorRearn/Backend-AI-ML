from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.schemas.cluster import ClusterResult
from app.services import cluster_service

router = APIRouter(prefix="/cluster", tags=["Cluster"])


@router.get("/traffy", response_model=List[ClusterResult])
def get_cluster_traffy(db: Session = Depends(get_db)):
    return cluster_service.get_cluster_data(db)
