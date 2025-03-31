from typing import Union, List, Any, Optional
import pandas as pd
import numpy as np

class Column:
    """
    A Column is a wrapper around pandas Series that provides a more intuitive interface
    for column operations.
    """
    
    def __init__(self, data: Union[pd.Series, List[Any], np.ndarray]):
        """
        Initialize a Column from various data sources.
        
        Args:
            data: Can be:
                - pandas Series
                - List of values
                - numpy array
        """
        if isinstance(data, pd.Series):
            self._series = data
        else:
            self._series = pd.Series(data)
    
    @property
    def name(self) -> str:
        """Get the name of the column."""
        return self._series.name
    
    @property
    def dtype(self) -> np.dtype:
        """Get the data type of the column."""
        return self._series.dtype
    
    @property
    def values(self) -> np.ndarray:
        """Get the values as a numpy array."""
        return self._series.values
    
    def head(self, n: int = 5) -> 'Column':
        """Return the first n values of the column."""
        return Column(self._series.head(n))
    
    def tail(self, n: int = 5) -> 'Column':
        """Return the last n values of the column."""
        return Column(self._series.tail(n))
    
    def unique(self) -> 'Column':
        """Return unique values in the column."""
        return Column(self._series.unique())
    
    def value_counts(self) -> 'Column':
        """Return value counts in the column."""
        return Column(self._series.value_counts())
    
    def isna(self) -> 'Column':
        """Return boolean mask of missing values."""
        return Column(self._series.isna())
    
    def notna(self) -> 'Column':
        """Return boolean mask of non-missing values."""
        return Column(self._series.notna())
    
    def fillna(self, value: Any) -> 'Column':
        """
        Fill missing values with a specified value.
        
        Args:
            value: Value to fill missing values with
        """
        return Column(self._series.fillna(value))
    
    def dropna(self) -> 'Column':
        """Drop missing values from the column."""
        return Column(self._series.dropna())
    
    def sort_values(self, ascending: bool = True) -> 'Column':
        """
        Sort values in the column.
        
        Args:
            ascending: Sort in ascending order if True
        """
        return Column(self._series.sort_values(ascending=ascending))
    
    def map(self, mapping: Union[dict, callable]) -> 'Column':
        """
        Map values using a dictionary or function.
        
        Args:
            mapping: Dictionary or function to map values
        """
        return Column(self._series.map(mapping))
    
    def apply(self, func: callable) -> 'Column':
        """
        Apply a function to each value in the column.
        
        Args:
            func: Function to apply
        """
        return Column(self._series.apply(func))
    
    def between(self, left: Any, right: Any, inclusive: str = 'both') -> 'Column':
        """
        Return boolean mask of values between left and right.
        
        Args:
            left: Left boundary
            right: Right boundary
            inclusive: Include boundaries ('both', 'left', 'right', 'neither')
        """
        return Column(self._series.between(left, right, inclusive=inclusive))
    
    def isin(self, values: List[Any]) -> 'Column':
        """
        Return boolean mask of values in the list.
        
        Args:
            values: List of values to check
        """
        return Column(self._series.isin(values))
    
    def to_pandas(self) -> pd.Series:
        """Convert the Column back to a pandas Series."""
        return self._series.copy()
    
    def __getitem__(self, key: Union[int, slice, List[bool]]) -> 'Column':
        """Get values by index, slice, or boolean mask."""
        return Column(self._series[key])
    
    def __len__(self) -> int:
        """Get the length of the column."""
        return len(self._series)
    
    def __repr__(self) -> str:
        """Get string representation of the column."""
        return f"Column({self._series})" 