#! usr/bin/python3

import pandas as pd

# exe 1
print("Reading csv......")
df = pd.read_csv('ws.csv')
print("Reading completed!")

# exe 2 & 3
# df.describe()
shape = df.shape
print("\n\nShape of the csv:\nRows:", shape[0], "\tColumns:", shape[1])
# print("Info:", df.info)

# exe 4
print("\nDropping the last column:'Info'")
# print(df.loc[:, 'Info'])
df.drop('Info', axis = 1, inplace=True)
# print(df.shape)
print("Column 'Info' is removed")

#exe 5

# exe 6
max_length = df.loc[:, 'Length'].max()
print(f"\nMaximun length of all packets is:{max_length}")

# exe 7
grouped = df.groupby(['Protocol'])
print("\nMean length of TCP packets length is:", grouped.mean()['Length']['TCP'])

# exe 8

