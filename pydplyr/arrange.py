from pandas import DataFrame

def arrange(df:DataFrame, column:str) -> DataFrame:
    """A simple arrange function that sorts values in a DataFrame based on a condition.

    Args:
        df: A pandas DataFrame
        condition: A string that represents the condition to sort the DataFrame
    
    Returns:
        A pandas DataFrame that has been sorted based on the condition
    """
    return df.sort_values(by=column)


if __name__ == "__main__":
    arrange()