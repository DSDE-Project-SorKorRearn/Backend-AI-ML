from pydantic import BaseModel

class MapPoint(BaseModel):
    latitude: float
    longitude: float
