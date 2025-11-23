from pydantic import BaseModel


class MapPoint(BaseModel):
    id: int
    latitude: float
    longitude: float
    traffy_type: str
