# Fix later download retail sales csv from canvas with wifi 
# Reflection Questions






print("---Exercise 1---")

import pandas as pd 
df = pd.read_csv('retail_sales.csv')
df.explore() 
# Inspection commands
print(df.head())
print(df.shape)
print(df.columns.tolist())
print(df.dtypes)

print("---Exercise 2---")
# Filtered 5000 rows. Resulting dataframe needs to show only 'South'
south = df[df['region'] == 'South'] # Does south equal region

print(len(south))
print(south.head())

print("---Exercise 3---")

top_5 = df.sort_values('revenue', ascending=False).head(5)
print(top_5)

print("---Exercise 4---")

big_south = df[(df['region'] == 'South') & (df['revenue'] > 1000)]
print(len(big_south))



print("---Exercise 5---")

df['per_unit'] = df['revenue'] / df['quantity']
print(df.head())

print("---Exercise 6---")

#Method 1 if we operate in a region
print(df['region'].unique())

#Method 2 how much business we do there 
print(df['region'].value_counts())

print("---Exercise 7---")

df_subset = df[['region', 'product', 'revenue']]
print(df_subset.shape)

print("---Exercise 8---")

df.to_csv('data/explored.csv', index=False)