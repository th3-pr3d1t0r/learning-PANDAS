import pandas as pd
import numpy as np

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

