import ast
from sqlalchemy.orm import Session
from sqlalchemy import func
from typing import Optional, Tuple, List
from app.db.models import Traffy


def parse_traffy_type_data(type_str: Optional[str]) -> Tuple[List[str], Optional[str]]:
    if not type_str:
        return ([], None)
    
    all_types = []
    primary_type = None
    
    try:
        parsed = ast.literal_eval(type_str)
        if isinstance(parsed, list):
            all_types = [str(t) for t in parsed if t is not None]
            if all_types:
                primary_type = all_types[0]
        elif parsed:
            
            primary_type = str(parsed)
            all_types = [primary_type]
            
    except (ValueError, SyntaxError, TypeError):
        primary_type = str(type_str)
        all_types = [primary_type]  
    return (all_types, primary_type)

def get_map_data(db: Session, type_name: Optional[str] = None):
    query = db.query(
        Traffy.index,
        Traffy.latitude,
        Traffy.longitude,
        Traffy.traffy_type
    )

    if type_name:
        query = query.filter(
            Traffy.traffy_type.ilike(f"%{type_name}%")
        )

    results = query.limit(10000).all()
    processed_data = []
    
    if type_name:
        type_name_lower = type_name.lower()
        
    for r in results:
        index, latitude, longitude, raw_type_str = r
        all_types, primary_type = parse_traffy_type_data(raw_type_str)
    
        if type_name:
            is_match = any(type_name_lower in t.lower() for t in all_types)
            if not is_match:
                continue 
            
            best_match = next((t for t in all_types if type_name_lower in t.lower()), None)
            
            if best_match:
                primary_type = best_match
        
        processed_data.append({
            "index": index, 
            "latitude": latitude, 
            "longitude": longitude, 
            "traffy_type": primary_type
        })
    return processed_data