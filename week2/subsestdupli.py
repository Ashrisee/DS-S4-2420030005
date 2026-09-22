import pandas as pd

df = pd.DataFrame({
    'id': [1, 2, 3, 2, 4, 1],
    'name': ['Asha', 'Ravi', 'Kiran', 'Rohit', 'Divya', 'Asha M'],
    'age': [21, 23, 22, 25, 24, 21]
})

print("OG dataset:")
print(df)

df_no_duplicates = df.drop_duplicates(subset=['id'])
print("After removing duplicates based on 'id':")
print(df_no_duplicates)