import pandas as pd

df = pd.DataFrame({
    'id': [1, 2, 3, 2, 4, 1],
    'name': ['Asha', 'Ravi', 'Kiran', 'Ravi', 'Divya', 'Asha'],
    'age': [21, 23, 22, 23, 24, 21]
})

print("OG dataset:")
print(df)

df_no_duplicates = df.drop_duplicates()
print("After removing duplicates:")
print(df_no_duplicates)