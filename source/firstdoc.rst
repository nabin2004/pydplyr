Guide to pydplyr
================

This guide will help you get started with `pydplyr`, showcasing its key features and how to use them effectively.

Getting Started
---------------

### Installation

Install `pydplyr` using pip:

.. code-block:: bash

    pip install pydplyr

### Importing the Library

To use `pydplyr`, import it as follows:

.. code-block:: python

    from pydplyr import arrange, select, filter, mutate, summarize

    # Example with Pandas
    import pandas as pd
    data = pd.DataFrame({
        'name': ['Alice', 'Bob', 'Charlie'],
        'age': [25, 30, 35],
        'score': [90, 85, 80]
    })

    # Arrange data by age
    arranged_data = arrange(data, by='age', ascending=True)

Five Verbs for Data Manipulation
--------------------------------

`pydplyr` provides a concise and expressive set of verbs for common data manipulation tasks:

1. **Arrange**: Sort rows by one or more columns.
2. **Select**: Choose specific columns.
3. **Filter**: Keep rows that meet certain conditions.
4. **Mutate**: Create new columns based on existing data.
5. **Summarize**: Aggregate data by groups or across the entire dataset.

### Example Usage

.. code-block:: python

    # Filter rows where age > 30
    filtered_data = filter(data, condition=lambda df: df['age'] > 30)

    # Mutate: Add a new column
    mutated_data = mutate(data, new_score=lambda df: df['score'] + 5)

Grammar of Graphics
-------------------

Create powerful visualizations using the grammar of graphics principles:

1. **Data**: The dataset to visualize.
2. **Aesthetics**: Mapping of data to visual properties (e.g., x, y, color).
3. **Geometries**: Shapes (e.g., points, lines, bars).
4. **Facets**: Subplots for different groups.
5. **Statistics**: Transformations or aggregations.
6. **Coordinates**: Customize axes and grid layouts.
7. **Themes**: Adjust visual styling.

### Example

.. code-block:: python

    from pydplyr.visuals import ggplot, aes, geom_bar

    # Create a bar plot
    plot = ggplot(data, aes(x='name', y='score')) + geom_bar()
    plot.show()

Simplified Regular Expressions
------------------------------

Work with regular expressions more intuitively with `pydplyr`'s simplified RegEx tools.

### Example

.. code-block:: python

    from pydplyr.regex import match

    # Match names starting with 'A'
    matches = match(data['name'], pattern='^A')
    print(matches)

Contributing
------------

We welcome contributions! Follow these steps to get started:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Submit a pull request with a clear description.

License
-------

This project is licensed under the MIT License. See the `LICENSE` file for more details.
