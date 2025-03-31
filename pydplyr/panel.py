from typing import Union, List, Dict, Any, Optional
import pandas as pd
import numpy as np
from .column import Column

class Panel:
    """
    A Panel is a wrapper around pandas DataFrame that provides a more intuitive interface
    for data manipulation operations.
    """
    
    def __init__(self, data: Union[pd.DataFrame, List[Dict[str, Any]], Dict[str, List[Any]]]):
        """
        Initialize a Panel from various data sources.
        
        Args:
            data: Can be:
                - pandas DataFrame
                - List of dictionaries
                - Dictionary of lists
        """
        if isinstance(data, pd.DataFrame):
            self._df = data
        else:
            self._df = pd.DataFrame(data)
    
    @property
    def columns(self) -> List[str]:
        """Get the column names of the Panel."""
        return list(self._df.columns)
    
    @property
    def shape(self) -> tuple:
        """Get the shape of the Panel (rows, columns)."""
        return self._df.shape
    
    def get_column(self, name: str) -> Column:
        """
        Get a column by name.
        
        Args:
            name: Name of the column to get
        """
        return Column(self._df[name])
    
    def head(self, n: int = 5) -> 'Panel':
        """Return the first n rows of the Panel."""
        return Panel(self._df.head(n))
    
    def tail(self, n: int = 5) -> 'Panel':
        """Return the last n rows of the Panel."""
        return Panel(self._df.tail(n))
    
    def select(self, columns: Union[str, List[str]]) -> 'Panel':
        """
        Select columns from the Panel.
        
        Args:
            columns: Single column name or list of column names
        """
        if isinstance(columns, str):
            columns = [columns]
        return Panel(self._df[columns])
    
    def filter(self, condition: str) -> 'Panel':
        """
        Filter rows based on a condition.
        
        Args:
            condition: String expression to evaluate (e.g., "age > 30")
        """
        return Panel(self._df.query(condition))
    
    def mutate(self, **kwargs) -> 'Panel':
        """
        Add or modify columns.
        
        Args:
            **kwargs: Column name and expression pairs
        """
        df = self._df.copy()
        for col, expr in kwargs.items():
            df[col] = eval(expr, {'df': df})
        return Panel(df)
    
    def arrange(self, columns: Union[str, List[str]], ascending: bool = True) -> 'Panel':
        """
        Sort the Panel by one or more columns.
        
        Args:
            columns: Column name or list of column names to sort by
            ascending: Sort in ascending order if True
        """
        if isinstance(columns, str):
            columns = [columns]
        return Panel(self._df.sort_values(columns, ascending=ascending))
    
    def group_by(self, columns: Union[str, List[str]]) -> 'GroupedPanel':
        """
        Group the Panel by one or more columns.
        
        Args:
            columns: Column name or list of column names to group by
        """
        if isinstance(columns, str):
            columns = [columns]
        return GroupedPanel(self._df.groupby(columns))
    
    def summarize(self, **kwargs) -> 'Panel':
        """
        Summarize the Panel by computing aggregations.
        
        Args:
            **kwargs: Column name and aggregation expression pairs
        """
        df = self._df.copy()
        for col, expr in kwargs.items():
            df[col] = eval(expr, {'df': df})
        return Panel(df)
    
    def inner_join(self, other: 'Panel', on: Optional[str] = None, 
                  left_on: Optional[str] = None, right_on: Optional[str] = None) -> 'Panel':
        """Perform an inner join with another Panel."""
        if on is not None:
            return Panel(pd.merge(self._df, other._df, on=on, how='inner'))
        elif left_on is not None and right_on is not None:
            return Panel(pd.merge(self._df, other._df, left_on=left_on, right_on=right_on, how='inner'))
        else:
            raise ValueError("Either 'on' or both 'left_on' and 'right_on' must be specified")
    
    def left_join(self, other: 'Panel', on: Optional[str] = None, 
                  left_on: Optional[str] = None, right_on: Optional[str] = None) -> 'Panel':
        """Perform a left join with another Panel."""
        if on is not None:
            return Panel(pd.merge(self._df, other._df, on=on, how='left'))
        elif left_on is not None and right_on is not None:
            return Panel(pd.merge(self._df, other._df, left_on=left_on, right_on=right_on, how='left'))
        else:
            raise ValueError("Either 'on' or both 'left_on' and 'right_on' must be specified")
    
    def right_join(self, other: 'Panel', on: Optional[str] = None, 
                   left_on: Optional[str] = None, right_on: Optional[str] = None) -> 'Panel':
        """Perform a right join with another Panel."""
        if on is not None:
            return Panel(pd.merge(self._df, other._df, on=on, how='right'))
        elif left_on is not None and right_on is not None:
            return Panel(pd.merge(self._df, other._df, left_on=left_on, right_on=right_on, how='right'))
        else:
            raise ValueError("Either 'on' or both 'left_on' and 'right_on' must be specified")
    
    def outer_join(self, other: 'Panel', on: Optional[str] = None, 
                   left_on: Optional[str] = None, right_on: Optional[str] = None) -> 'Panel':
        """Perform an outer join with another Panel."""
        if on is not None:
            return Panel(pd.merge(self._df, other._df, on=on, how='outer'))
        elif left_on is not None and right_on is not None:
            return Panel(pd.merge(self._df, other._df, left_on=left_on, right_on=right_on, how='outer'))
        else:
            raise ValueError("Either 'on' or both 'left_on' and 'right_on' must be specified")
    
    def to_pandas(self) -> pd.DataFrame:
        """Convert the Panel back to a pandas DataFrame."""
        return self._df.copy()

class GroupedPanel:
    """
    A class to handle grouped operations on a Panel.
    """
    
    def __init__(self, grouped_df):
        self._grouped = grouped_df
    
    def summarize(self, **kwargs) -> Panel:
        """
        Summarize each group by computing aggregations.
        
        Args:
            **kwargs: Column name and aggregation expression pairs
        """
        return Panel(self._grouped.agg(kwargs).reset_index()) 