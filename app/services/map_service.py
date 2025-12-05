import ast
from sqlalchemy.orm import Session
from sqlalchemy import func
from typing import Optional, Tuple, List
from app.db.models import Traffy


def parse_traffy_type_data(type_str: Optional[str]) -> Tuple[List[str], Optional[str]]:
    """
    Safely parses a raw type string.
    Returns: (list_of_all_types, primary_type_for_display)
    """
    if not type_str:
        return ([], None)
    
    all_types = []
    primary_type = None
    
    try:
        # Use ast.literal_eval to safely convert the string list to a Python list
        parsed = ast.literal_eval(type_str)
        
        if isinstance(parsed, list):
            # If it's a list, flatten all types and set the first as primary
            all_types = [str(t) for t in parsed if t is not None]
            if all_types:
                primary_type = all_types[0]
        elif parsed:
            # If it's a single item, use it as both
            primary_type = str(parsed)
            all_types = [primary_type]
            
    except (ValueError, SyntaxError, TypeError):
        # Fallback for plain string that failed to parse
        primary_type = str(type_str)
        all_types = [primary_type]
        
    return (all_types, primary_type)



    

def get_map_data(db: Session, type_name: Optional[str] = None):
    # STEP 1: Define the base query
    query = db.query(
        Traffy.index,
        Traffy.latitude,
        Traffy.longitude,
        Traffy.traffy_type
    )
    
    # STEP 2: Apply the filter at the database level BEFORE the limit
    if type_name:
        # Use ilike (case-insensitive LIKE) to check if the raw string contains the type_name.
        # The wildcard % is necessary for substring matching.
        # This significantly reduces the data set before the Python filter runs.
        query = query.filter(
            Traffy.traffy_type.ilike(f"%{type_name}%")
        )

    # STEP 3: Apply the limit now that the records are relevant
    results = query.limit(10000).all()
    
    processed_data = []
    
    if type_name:
        type_name_lower = type_name.lower()
        
    for r in results:
        index, latitude, longitude, raw_type_str = r
        all_types, primary_type = parse_traffy_type_data(raw_type_str)
    
        if type_name:
            # STEP 4A: Accurate Python-side substring check
            is_match = any(type_name_lower in t.lower() for t in all_types)
            if not is_match:
                continue 
                
            # STEP 4B: Override primary_type to the filtered type for display
            # Find the best matching type from all_types to use as primary_type
            best_match = next((t for t in all_types if type_name_lower in t.lower()), None)
            
            if best_match:
                primary_type = best_match # This ensures the output matches the filter
        
        processed_data.append({
            "index": index, 
            "latitude": latitude, 
            "longitude": longitude, 
            "traffy_type": primary_type
        })
        
    return processed_data