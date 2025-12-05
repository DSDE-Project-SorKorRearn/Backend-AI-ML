from fastapi import APIRouter, HTTPException, Response
from app.config import settings

router = APIRouter(prefix="/cluster", tags=["Cluster"])

@router.get("/traffy")
def get_cluster_traffy():
    try:
        return Response(content=settings.CLUSTER_CACHE, media_type="text/csv")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



