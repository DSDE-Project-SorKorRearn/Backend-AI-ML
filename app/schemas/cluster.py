from pydantic import BaseModel

class ClusterResult(BaseModel):
    province: str
    district: str
    cluster_id: int
    count: int
