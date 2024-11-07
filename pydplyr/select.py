from pandas import DataFrame 

def select(df:DataFrame, *columns:str)-> DataFrame:
    """
    A simple select function that returns a DataFrame with only the specified columns.

    Args:
        df: A pandas DataFrame.
        *columns: Column names to select from the DataFrame.
    
    Returns:
        A pandas DataFrame containing only the specified columns.
    """
    return df[list(columns)]


if __name__ == "__main__":
    select()
