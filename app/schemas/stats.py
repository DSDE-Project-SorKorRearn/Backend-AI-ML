from pydantic import BaseModel
from typing import List
class TimeSeriesData(BaseModel):
    year: str
    month: str
    count: int

class ProvinceData(BaseModel):
    province: str
    count: int

class DistrictData(BaseModel):
    district: str
    count: int

class TypeData(BaseModel):
    traffy_type: str
    count: int