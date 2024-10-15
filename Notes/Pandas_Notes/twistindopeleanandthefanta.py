import pandas as pd
#concatenating two data frames
df = pd.read_csv('heart.csv').head()
df2 = pd.read_csv('heart.csv').tail()
result = pd.concat([df,df2]) #concatenating rows
print(result) #this will not reset indexes
result = pd.concat([df,df2], ignore_index=True) #ignore_index = True allows us to reset indexes when we concat dataframes
print(result)
df=df[['age','sex','cp','trestbps','chol','fbs','restecg','thalach','exang','oldpeak',]]
df2=df2[['slope','ca','thal','target']]
result = pd.concat([df,df2], axis = "columns") #usually rows concat will have ignore_index set to true because ideally we would want to reset indexes but for columns we don't want to change the labels
print(result)
result.reset_index(drop = True, inplace=True)
print(result)
result = pd.concat([df,df2], axis = "columns", ignore_index=True) #this will change column labels to numberings starting from 0
print(result)
print(df[['age']]) #extraction of particular col
print(df[['age', 'sex']]) #extraction of multiple cols
print(df)
print(df.loc[1][3]) #iloc[][] allows access to rows and columns by indexes (might give Future Warning since method is modified in pandas 3.0)
print(df.loc[1]['trestbps']) #loc[][] allows access to rows and columns by labels
print(df.loc[df['age']>60]) #df[df['age']>60] prints the same thing
names = ['A','B','C','D','E']
df.insert(2,'name',names)
print(df)
df = df.set_index('name') #sets the name columns as the index
print(df)
df.sort_values('age', inplace=True)
print(df)
print(df.at['A', 'age']) #returns value at that pos
df.at['A', 'age'] = 100
print(df)

#derived columns can be made
df['new col'] = df['age'] + df['thalach'] #Col values are added for each particular position
print(df)
