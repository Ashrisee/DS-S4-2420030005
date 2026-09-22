import pandas as pd

df = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'name': [' Asha ', 'ravi', 'KIRAN', 'Divya '],
    'department': ['hr', 'FINANCE', ' Finance ', 'it']
})

print("OG dataset:")
print(df)

# Standardize: strip extra spaces + consistent casing (title case)
df['name'] = df['name'].str.strip().str.title()
df['department'] = df['department'].str.strip().str.upper()

print("After standardization:")
print(df)
