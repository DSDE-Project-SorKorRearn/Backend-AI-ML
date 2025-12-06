from fastapi import APIRouter, HTTPException, Response
from app.config import settings

router = APIRouter(prefix="/cluster", tags=["Cluster"])

@router.get("/traffy")
def get_cluster_traffy(district: str):
    try:
        df = settings.CLUSTER_DF[settings.CLUSTER_DF["district"] == district]
        csv_cache = df.to_csv(index=False).encode('utf-8')
        return Response(content=csv_cache, media_type="text/csv")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



