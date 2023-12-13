import pandas as pd

df = pd.read_csv("xy.csv", encoding='cp1252')
for i, x in df.groupby('Cardholder Name'): x.to_csv(f'{i}.csv', index=False)

# for i, x in df.groupby('Account Number'): x.to_csv(f'Schedule of account {i} for FY 2022 - Eco Insects.csv',
# index=False)