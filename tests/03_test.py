import pandas as pd
import pytest
from pydplyr.panel import Panel
from pydplyr.inner_join import inner_join
from pydplyr.left_join import left_join
from pydplyr.right_join import right_join
from pydplyr.outer_join import outer_join

def test_inner_join():
    # Arrange
    left_df = Panel(pd.DataFrame({'A': [1, 2, 3], 'B': ['a', 'b', 'c']}))
    right_df = Panel(pd.DataFrame({'A': [2, 3, 4], 'C': ['x', 'y', 'z']}))
    
    # Act
    result = inner_join(left_df, right_df, on='A')
    
    # Assert
    assert len(result._df) == 2, "Inner join should only include matching rows"
    assert list(result._df['A']) == [2, 3], "Joined values should be [2, 3]"
    assert 'B' in result.columns, "Left table columns should be preserved"
    assert 'C' in result.columns, "Right table columns should be preserved"

def test_left_join():
    # Arrange
    left_df = Panel(pd.DataFrame({'A': [1, 2, 3], 'B': ['a', 'b', 'c']}))
    right_df = Panel(pd.DataFrame({'A': [2, 3, 4], 'C': ['x', 'y', 'z']}))
    
    # Act
    result = left_join(left_df, right_df, on='A')
    
    # Assert
    assert len(result._df) == 3, "Left join should include all left table rows"
    assert list(result._df['A']) == [1, 2, 3], "All left table values should be preserved"
    assert pd.isna(result._df.loc[result._df['A'] == 1, 'C'].iloc[0]), "Non-matching rows should have NaN values"

def test_right_join():
    # Arrange
    left_df = Panel(pd.DataFrame({'A': [1, 2, 3], 'B': ['a', 'b', 'c']}))
    right_df = Panel(pd.DataFrame({'A': [2, 3, 4], 'C': ['x', 'y', 'z']}))
    
    # Act
    result = right_join(left_df, right_df, on='A')
    
    # Assert
    assert len(result._df) == 3, "Right join should include all right table rows"
    assert list(result._df['A']) == [2, 3, 4], "All right table values should be preserved"
    assert pd.isna(result._df.loc[result._df['A'] == 4, 'B'].iloc[0]), "Non-matching rows should have NaN values"

def test_outer_join():
    # Arrange
    left_df = Panel(pd.DataFrame({'A': [1, 2, 3], 'B': ['a', 'b', 'c']}))
    right_df = Panel(pd.DataFrame({'A': [2, 3, 4], 'C': ['x', 'y', 'z']}))
    
    # Act
    result = outer_join(left_df, right_df, on='A')
    
    # Assert
    assert len(result._df) == 4, "Outer join should include all rows from both tables"
    assert sorted(list(result._df['A'])) == [1, 2, 3, 4], "All values from both tables should be included"
    assert pd.isna(result._df.loc[result._df['A'] == 1, 'C'].iloc[0]), "Non-matching rows should have NaN values"
    assert pd.isna(result._df.loc[result._df['A'] == 4, 'B'].iloc[0]), "Non-matching rows should have NaN values"

def test_join_with_different_column_names():
    # Arrange
    left_df = Panel(pd.DataFrame({'A': [1, 2, 3], 'B': ['a', 'b', 'c']}))
    right_df = Panel(pd.DataFrame({'X': [2, 3, 4], 'C': ['x', 'y', 'z']}))
    
    # Act
    result = inner_join(left_df, right_df, left_on='A', right_on='X')
    
    # Assert
    assert len(result._df) == 2, "Join should work with different column names"
    assert list(result._df['A']) == [2, 3], "Joined values should be [2, 3]"

def test_join_with_empty_dataframes():
    # Arrange
    left_df = Panel(pd.DataFrame(columns=['A', 'B']))
    right_df = Panel(pd.DataFrame(columns=['A', 'C']))
    
    # Act
    result = inner_join(left_df, right_df, on='A')
    
    # Assert
    assert len(result._df) == 0, "Join of empty dataframes should be empty"
    assert list(result.columns) == ['A', 'B', 'C'], "Columns should be preserved"

if __name__ == "__main__":
    pytest.main() 