import pandas as pd
import numpy as np

df = pd.DataFrame({ 'Age': [25, 30, np.nan, 40, 35],
    'department': ['HR' , 'Finance', 'Finance', np.nan, 'IT']})

print("OG dataset:")
print(df)

# Drop rows with any null values
df_row_dropped = df.dropna(axis=0)
print("After dropping rows with nulls:")
print(df_row_dropped)

# Drop columns with any null values
df_col_dropped = df.dropna(axis=1)
print("After dropping columns with nulls:")
print(df_col_dropped)