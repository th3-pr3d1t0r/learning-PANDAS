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

# ---------------------------
# 11. Convert column to different dtype
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

# ---------------------------
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

# ---------------------------
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

# ---------------------------
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

# ---------------------------
# 31. Reset index after drop
df.reset_index(drop=True, inplace=True)
print(df.head())

# 32. Insert column at specific location
df.insert(1, 'Zeta', ['a', 'b', 'c', 'd'])
print(df.head())

# 33. Map values
df['Gamma'] = df['Gamma'].map({'foo': 1, 'bar': 2, 'baz': 3})
print(df.head())

# 34. Replace values
df['Gamma'] = df['Gamma'].replace(1, 100)
print(df.head())

# 35. Fill NA values
df['Gamma'] = df['Gamma'].fillna(0)
print(df.head())

# ---------------------------
# 36. Drop rows with NA
print(df.dropna())

# 37. Count values in a column
print(df['Gamma'].value_counts())

# 38. Unique values
print(df['Gamma'].unique())

# 39. Number of unique values
print(df['Gamma'].nunique())

# 40. Check if value exists
print(100 in df['Gamma'].values)

# ---------------------------
# 41. Apply function to column
df['Alpha'] = df['Alpha'].apply(lambda x: x * 2)
print(df.head())

# 42. Apply function to entire DataFrame
print(df.applymap(lambda x: str(x) + '_new'))

# 43. Group by and aggregate
print(df.groupby('Gamma').mean())

# 44. Group by multiple columns
print(df.groupby(['Gamma']).sum())

# 45. Aggregate with multiple functions
print(df.groupby('Gamma').agg({'Alpha': ['mean', 'max']}))

# ---------------------------
# 46. Cumulative sum
print(df['Alpha'].cumsum())

# 47. Cumulative product
print(df['Beta'].cumprod())

# 48. Rank
print(df['Beta'].rank())

# 49. Rolling mean
print(df['Beta'].rolling(2).mean())

# 50. Expanding mean
print(df['Beta'].expanding(2).mean())

# ---------------------------
# 51. Pivot table
print(df.pivot_table(values='Alpha', index='Gamma', aggfunc='mean'))

# 52. Melting
df_melted = pd.melt(df, id_vars=['Gamma'], value_vars=['Alpha', 'Beta'])
print(df_melted.head())

# 53. Concatenating two DataFrames
df2 = df.copy()
df_concat = pd.concat([df, df2])
print(df_concat.head())

# 54. Merging two DataFrames
df3 = pd.DataFrame({'Gamma': [100, 2], 'NewCol': ['x', 'y']})
df_merged = pd.merge(df, df3, on='Gamma', how='left')
print(df_merged.head())

# 55. Join on index
df4 = pd.DataFrame({'NewIndex': [0,1,2,3]}, index=df.index)
df_joined = df.join(df4)
print(df_joined.head())

# ---------------------------
# 56. MultiIndex from columns
df_multi = df.set_index(['Gamma', 'Beta'])
print(df_multi.head())

# 57. Swap MultiIndex levels
print(df_multi.swaplevel(0,1).head())

# 58. Reset index on MultiIndex
print(df_multi.reset_index())

# 59. Stack columns
print(df.stack())

# 60. Unstack index
print(df_multi.unstack())

# ---------------------------
# 61. Filter using isin
print(df[df['Gamma'].isin([100])])

# 62. Clip values
print(df['Beta'].clip(lower=7, upper=8))

# 63. Sample random rows
print(df.sample(2))

# 64. Shuffle DataFrame
print(df.sample(frac=1).reset_index(drop=True))

# 65. Drop duplicates
df_dup = pd.concat([df, df.iloc[0:1]])
print(df_dup.drop_duplicates())

# ---------------------------
# 66. Set with loc
df.loc[1, 'Beta'] = 99
print(df.head())

# 67. Mask values
print(df['Beta'].mask(df['Beta'] > 90, 0))

# 68. Where condition
print(df['Beta'].where(df['Beta'] > 90, -1))

# 69. Shift values
print(df['Beta'].shift(1))

# 70. Diff between rows
print(df['Beta'].diff())

# ---------------------------
# 71. Datetime to year
print(df['D'].dt.year)

# 72. Datetime to month
print(df['D'].dt.month)

# 73. Datetime to day
print(df['D'].dt.day)

# 74. Datetime weekday
print(df['D'].dt.weekday)

# 75. Create date range
print(pd.date_range('2025-01-01', periods=5))

# ---------------------------
# 76. String lower
print(df['Zeta'].str.lower())

# 77. String upper
print(df['Zeta'].str.upper())

# 78. String contains
print(df['Zeta'].str.contains('a'))

# 79. String length
print(df['Zeta'].str.len())

# 80. Split string
print(df['Zeta'].str.split('a'))

# ---------------------------
# 81. Convert to JSON
print(df.to_json())

# 82. Convert to dict
print(df.to_dict())

# 83. Convert to CSV string
print(df.to_csv(index=False))

# 84. Save to CSV file
df.to_csv('example.csv', index=False)

# 85. Read from CSV file
df_from_csv = pd.read_csv('example.csv')
print(df_from_csv.head())

# ---------------------------
# 86. Style DataFrame
print(df.style.highlight_max(axis=0))

# 87. Check memory usage
print(df.memory_usage())

# 88. Find correlations
print(df[['Alpha', 'Beta']].corr())

# 89. Covariance
print(df[['Alpha', 'Beta']].cov())

# 90. Skewness
print(df[['Alpha', 'Beta']].skew())

# ---------------------------
# 91. Kurtosis
print(df[['Alpha', 'Beta']].kurt())

# 92. Count non-NA
print(df.count())

# 93. Transpose DataFrame
print(df.T)

# 94. Set categories
df['Zeta'] = df['Zeta'].astype('category')
print(df['Zeta'].cat.categories)

# 95. Add category level
df['Zeta'] = df['Zeta'].cat.add_categories(['e'])
print(df['Zeta'].cat.categories)

# ---------------------------
# 96. Filter category
print(df[df['Zeta'] == 'a'])

# 97. Value counts with normalize
print(df['Zeta'].value_counts(normalize=True))

# 98. Multi aggregation
print(df.agg({'Alpha': ['min', 'max'], 'Beta': ['sum']}))

# 99. Clip lower only
print(df['Beta'].clip(lower=7))

# 100. Replace using regex
print(df['Zeta'].str.replace('a', 'X', regex=True))
