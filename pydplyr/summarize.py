from pandas import DataFrame

def summarize(df:DataFrame)-> DataFrame:
    """A simple summarize function that info about the dataframe.

    Args:
        df: A pandas DataFrame

    Returns:
        Info about the dataframe
    """
    return df.info()


if __name__ == "__main__":
    summarize()
