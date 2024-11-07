from pandas import DataFrame
from typing import List, Optional

def distinct(df: DataFrame, columns: Optional[List[str]] = None) -> DataFrame:
    """
    A distinct function that returns a DataFrame with unique rows based on specified columns.

    Args:
        df: A pandas DataFrame.
        columns: Optional; a list of column names to consider for uniqueness.
                 If None, all columns are considered.
    
    Returns:
        A pandas DataFrame with unique rows based on the specified columns.
    """
    if columns:
        return df.drop_duplicates(subset=columns)
    else:
        return df.drop_duplicates()
    
if __name__ == "__main__":
    distinct()