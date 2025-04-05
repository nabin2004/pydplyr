import pandas as pd
from typing import List, Optional
from pydplyr.arrange import asc, desc

class Panel:
    def __init__(self, df):
        self.df = df

    def arrange(self, *args): 
        from pydplyr.arrange import arrange
        return Panel(arrange(self.df, *args))

    def filter(self, expr):
        from pydplyr.filter import filter
        return Panel(filter(self.df, expr))

    def mutate(self, **kwargs):
        """
        Creates new columns based on expressions.
        
        Args:
            **kwargs: Keyword arguments where the key is the new column name and the value is the expression.
                      The expression can be a string representing a valid operation, e.g., "score + age".
        
        Returns:
            A new Panel with the modified DataFrame containing the new columns.
        """
        from pydplyr.mutate import mutate
        return Panel(mutate(self.df, **kwargs))
    
    def select(self, *cols):
        from pydplyr.select import select
        return Panel(select(self.df, *cols))

    def summarize(self, **kwargs):
        from pydplyr.summarize import summarize
        return summarize(self.df, **kwargs) 
    
    def distinct(self, columns: Optional[List[str]] = None) -> "Panel":
        """
        Removes duplicate rows based on the specified columns (or all columns by default).

        Args:
            columns: Optional list of column names to check for uniqueness.
        
        Returns:
            A new Panel with the distinct rows.
        """
        from pydplyr.distinct import distinct
        df = distinct(self.df, columns)
        return Panel(df)

    def collect(self):
        return self.df
