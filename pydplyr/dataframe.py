import pandas as pd

class Dataframe(pd.DataFrame):

    def __init__(self, *args, custom_property=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.custom_property = custom_property

    def select(self, *columns):
        """Select specific columns from the DataFrame."""
        return self[columns]

    def filter(self, condition):
        """Filter rows based on a condition."""
        return self.query(condition)

    def mutate(self, column_name, data):
        """Add a new column to the DataFrame."""
        self[column_name] = data

    def __repr__(self):
        return f"CustomDataFrame(custom_property={self.custom_property})\n{super().__repr__()}"
