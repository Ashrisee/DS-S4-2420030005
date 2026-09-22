import pandas as pd
import numpy as np

df = pd.DataFrame({ 'Age': [25, 30, np.nan, 40, 35],
    'department': ['HR' , 'Finance', 'Finance', np.nan, 'IT']})

print("OG dataset:")
print(df)

# Forward fill first
df['Age'] = df['Age'].ffill()
df['department'] = df['department'].ffill()

print("After forward fill:")
print(df)

# Backward fill next (catches any nulls ffill couldn't fill, e.g. if first row was null)
df['Age'] = df['Age'].bfill()
df['department'] = df['department'].bfill()

print("After backward fill:")
print(df)