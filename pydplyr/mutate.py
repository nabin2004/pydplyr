from pandas import DataFrame

def mutate(df: DataFrame, **kwargs) -> DataFrame:
    """
    Creates new columns based on expressions.
    
    Args:
        df: A pandas DataFrame.
        **kwargs: Keyword arguments where the key is the new column name and the value is the expression.
                  The expression can be a string representing a valid operation (e.g., "score + age").
    
    Returns:
        A new pandas DataFrame with the modified columns.
    """
    for col, expr in kwargs.items():
        df[col] = df.eval(expr)
    return df


if __name__ == "__main__":
    mutate()
