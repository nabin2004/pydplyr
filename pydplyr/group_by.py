from pandas import DataFrame
from typing import List

def group_by(df: DataFrame, *columns: str) -> DataFrame:
    """
    A group_by function that groups a DataFrame by one or more columns.

    Args:
        df: A pandas DataFrame.
        *columns: Column names to group by.
    
    Returns:
        A pandas GroupBy object.
    """
    return df.groupby(list(columns))

if __name__ == "__main__":
    group_by()