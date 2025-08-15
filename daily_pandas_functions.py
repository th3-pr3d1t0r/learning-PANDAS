import pandas as pd
import numpy as np
#random comment 
# Sample DataFrame
df = pd.DataFrame({
    'A': [1, 2, 3, 4, 5],
    'B': [5, 6, 7, 8, 9],
    'C': ['foo', 'bar', 'foo', 'baz', 'bar'],
    'D': pd.date_range('2025-01-01', periods=5)
})

# ---------------------------
# 1. View first few rows
print(df.head())

# 2. View last few rows
print(df.tail())

# 3. Get shape of DataFrame
print(df.shape)

# 4. Get column names
print(df.columns)

# 5. Get index
print(df.index)

# 6. Basic info
print(df.info())

# 7. Summary statistics
print(df.describe())

# 8. Check for missing values
print(df.isnull())

# 9. Count missing values per column
print(df.isnull().sum())

# 10. Check data types
print(df.dtypes)

# 11. Convert column to different dtype
df['A'] = df['A'].astype(float)
print(df.dtypes)
df['A'] = df['A'].astype(float)
print(df.dtypes)
# 12. Rename a single column
df.rename(columns={'A': 'Alpha'}, inplace=True)
print(df.head())

# 13. Rename multiple columns
df.rename(columns={'B': 'Beta', 'C': 'Gamma'}, inplace=True)
print(df.head())

# 14. Set a column as index
df.set_index('D', inplace=True)
print(df.head())

# 15. Reset index back to default
df.reset_index(inplace=True)
print(df.head())

# 16. Selecting a single column
print(df['Alpha'])

# 17. Selecting multiple columns
print(df[['Alpha', 'Beta']])

# 18. Selecting rows by position
print(df.iloc[2])

# 19. Selecting rows by index label
print(df.loc[2])

# 20. Selecting specific rows and columns
print(df.loc[2, 'Beta'])

# 21. Conditional selection
print(df[df['Beta'] > 6])

# 22. Filter with multiple conditions
print(df[(df['Beta'] > 6) & (df['Gamma'] == 'foo')])

# 23. Using query
print(df.query('Beta > 6'))

# 24. Sort by a column ascending
print(df.sort_values('Beta'))

# 25. Sort by a column descending
print(df.sort_values('Beta', ascending=False))

# 26. Add a new column (static value)
df['Delta'] = 10
print(df.head())

# 27. Add a new column (based on other columns)
df['Epsilon'] = df['Alpha'] + df['Beta']
print(df.head())

# 28. Drop a single column
df.drop('Delta', axis=1, inplace=True)
print(df.head())

# 29. Drop multiple columns
df.drop(['Epsilon'], axis=1, inplace=True)
print(df.head())

# 30. Drop a row by index
df.drop(0, axis=0, inplace=True)
print(df.head())

# 31. Reset index after drop
df.reset_index(drop=True, inplace=True)
print(df.head())

# 32. Insert column at specific location
df.insert(1, 'Zeta', ['a', 'b', 'c', 'd'])
print(df.head())

