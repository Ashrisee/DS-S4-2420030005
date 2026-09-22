import pandas as pd
import numpy as np
df = pd.DataFrame({ 'Age': [25, 30, np.nan, 40, 35],
    'department': ['HR' , 'Finance', 'Finance',np.nan, 'IT']})
print("OG dataset:")
print(df)
df['Age'] = df['Age'].fillna(df['Age'].mean())
df['department'] = df['department'].fillna(df['department'].mode()[0])
print(df)