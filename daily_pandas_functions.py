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

