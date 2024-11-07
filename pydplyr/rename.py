# this function is may be not required,as it is same in pandas 
from pandas import DataFrame
from typing import Dict

def rename(df: DataFrame, columns: Dict[str, str]) -> DataFrame:
    """
    A rename function that renames columns in the DataFrame.

    Args:
        df: A pandas DataFrame.
        columns: A dictionary where keys are current column names, and values are new column names.
    
    Returns:
        A pandas DataFrame with columns renamed.
    """
    return df.rename(columns=columns)

if __name__ == "__main__":
    rename()
