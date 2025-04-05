from pandas import DataFrame
from typing import Union, List, Tuple

def asc(col: str) -> Tuple[str, bool]:
    """Returns a tuple for ascending sort."""
    return col, True

def desc(col: str) -> Tuple[str, bool]:
    """Returns a tuple for descending sort."""
    return col, False

def arrange(df: DataFrame, *args: Union[str, Tuple[str, bool]]) -> DataFrame:
    """
    A simple arrange function that sorts values in a DataFrame based on one or more columns.
    The first argument can be a string filter expression (e.g., "score > 80"), followed by columns for sorting.
    
    Args:
        df: A pandas DataFrame.
        *args: First argument can be a string filter expression (e.g., "score > 80").
              The following arguments are column names or tuples like ('col', ascending_bool).
    
    Returns:
        A pandas DataFrame sorted by the given columns and optionally filtered by the expression.
    """

    if isinstance(args[0], str) and any(op in args[0] for op in ['>', '<', '==', '!=', '>=', '<=', '&', '|']):
        string_exp = args[0]
        args = args[1:] 
        df = df.query(string_exp)
    else:
        string_exp = None 
    
    by = []
    ascending = []
    
    for col in args:
        if isinstance(col, tuple):
            by.append(col[0])
            ascending.append(col[1])
        else:
            by.append(col)
            ascending.append(True)  
    
    return df.sort_values(by=by, ascending=ascending)
