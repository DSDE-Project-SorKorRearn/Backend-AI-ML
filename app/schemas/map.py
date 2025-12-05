from pydantic import BaseModel
from typing import Optional

class MapPoint(BaseModel):
    index: int
    latitude: float
    longitude: float
    traffy_type: Optional[str]
