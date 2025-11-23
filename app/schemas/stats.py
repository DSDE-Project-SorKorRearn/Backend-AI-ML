from pydantic import BaseModel

class TimeSeriesData(BaseModel):
    year: int
    month: int
    count: int

class ProvinceData(BaseModel):
    province: str
    count: int

class DistrictData(BaseModel):
    district: str
    count: int
