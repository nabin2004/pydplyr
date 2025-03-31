import pandas as pd
import pytest
from pydplyr.filter import filter
from pydplyr.select import select
from pydplyr.mutate import mutate
from pydplyr.group_by import group_by
from pydplyr.summarize import summarize
from pydplyr.distinct import distinct
from pydplyr.rename import rename

def test_filter():
    # Arrange
    data = {'A': [1, 2, 3, 4], 'B': ['a', 'b', 'c', 'd']}
    df = pd.DataFrame(data)
    
    # Act
    result = filter(df, 'A > 2')
    
    # Assert
    assert len(result) == 2, "Failed to filter rows where A > 2"
    assert result['A'].tolist() == [3, 4], "Filtered values are incorrect"

def test_select():
    # Arrange
    data = {'A': [1, 2, 3], 'B': ['a', 'b', 'c'], 'C': [4, 5, 6]}
    df = pd.DataFrame(data)
    
    # Act
    result = select(df, ['A', 'C'])
    
    # Assert
    assert list(result.columns) == ['A', 'C'], "Failed to select specified columns"
    assert len(result) == 3, "Row count should remain the same"

def test_mutate():
    # Arrange
    data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
    df = pd.DataFrame(data)
    
    # Act
    result = mutate(df, 'C = A + B')
    
    # Assert
    assert 'C' in result.columns, "New column 'C' was not created"
    assert result['C'].tolist() == [5, 7, 9], "Column 'C' values are incorrect"

def test_group_by():
    # Arrange
    data = {'A': [1, 1, 2, 2], 'B': [10, 20, 30, 40]}
    df = pd.DataFrame(data)
    
    # Act
    result = group_by(df, 'A')
    
    # Assert
    assert len(result.groups) == 2, "Failed to create correct number of groups"
    assert list(result.groups.keys()) == [1, 2], "Group keys are incorrect"

def test_summarize():
    # Arrange
    data = {'A': [1, 2, 3, 4], 'B': [10, 20, 30, 40]}
    df = pd.DataFrame(data)
    
    # Act
    result = summarize(df, {'B': 'mean'})
    
    # Assert
    assert 'B_mean' in result.columns, "Summary column was not created"
    assert result['B_mean'].iloc[0] == 25.0, "Mean calculation is incorrect"

def test_distinct():
    # Arrange
    data = {'A': [1, 1, 2, 2], 'B': ['a', 'a', 'b', 'b']}
    df = pd.DataFrame(data)
    
    # Act
    result = distinct(df, ['A'])
    
    # Assert
    assert len(result) == 2, "Failed to remove duplicate rows"
    assert result['A'].tolist() == [1, 2], "Distinct values are incorrect"

def test_rename():
    # Arrange
    data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
    df = pd.DataFrame(data)
    
    # Act
    result = rename(df, {'A': 'X', 'B': 'Y'})
    
    # Assert
    assert 'X' in result.columns, "Column 'A' was not renamed to 'X'"
    assert 'Y' in result.columns, "Column 'B' was not renamed to 'Y'"
    assert 'A' not in result.columns, "Original column 'A' still exists"
    assert 'B' not in result.columns, "Original column 'B' still exists"

if __name__ == "__main__":
    pytest.main() 