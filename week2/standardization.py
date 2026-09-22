import pandas as pd

df = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'name': ['Asha', 'Ravi', 'Kiran', 'Divya'],
    'join_date': ['12/05/2021', '2022-08-15', '5-Jan-2020', '01/30/2023']
})

print("OG dataset:")
print(df)

# Standardize all dates to one consistent format (YYYY-MM-DD)
df['join_date'] = pd.to_datetime(df['join_date'], dayfirst=False, errors='coerce')

print("After standardization:")
print(df)
print(df.dtypes)