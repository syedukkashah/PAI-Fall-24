import pandas as pd
import numpy as np
df = pd.DataFrame([[1,2,3], [4,5,6], [7,8,9]], columns=["A", "B", "C"], index=["x","y","z"])
print(df.describe)
print(df.shape)
df = pd.read_csv("friends.csv")
print(df)
df['new col'] = 100*df['num']
df['marks'] = np.round(df['marks'], 2)
print(df)
df = df.drop('marks', axis=1) #param(col, axis)
print(df)
print(df.index)
df = df.set_index('name')
print(df)
df = df.reset_index()
print(df)
print(df.iloc[0])
df = df.set_index('name')
print(df.loc[['Ramis','Ibrahim']])
print(df.at[0,"city"])
#concatenation of Data Frames
data_one = {'A':['A0', 'A1', 'A2', 'A3'], 'B': ['B0', 'B1', 'B2', 'B3']}
data_two = {'C':['C0', 'C1', 'C2', 'C3'], 'D': ['D0', 'D1', 'D2', 'D3']}
one = pd.DataFrame(data_one)
two = pd.DataFrame(data_two)
print(one)
print(two)
axis0=pd.concat([one,two], axis=0) #concat along rows
print(axis0)
axis1=pd.concat([one,two], axis=1) #concat along cols
print(axis1)
two.columns = one.columns #axis 0, but cols match up
print(pd.concat([one,two]))
