from fastapi import Query
from typing import Optional

def filter_params(
    year: Optional[int] = Query(None),
    month: Optional[int] = Query(None),
    province: Optional[str] = Query(None)
):
    return {"year": year, "month": month, "province": province}
