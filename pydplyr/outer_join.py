from typing import Optional
from .panel import Panel

def outer_join(left_df: Panel, right_df: Panel, on: Optional[str] = None, 
               left_on: Optional[str] = None, right_on: Optional[str] = None) -> Panel:
    """
    Perform an outer join between two Panels.
    
    Args:
        left_df: Left Panel
        right_df: Right Panel
        on: Column name to join on if both Panels have the same column name
        left_on: Column name from left Panel to join on
        right_on: Column name from right Panel to join on
        
    Returns:
        Panel containing the outer join result
    """
    return left_df.outer_join(right_df, on=on, left_on=left_on, right_on=right_on)
