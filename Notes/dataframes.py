import pandas as pd
registrations = pd.DataFrame({'reg_id':[1,2,3,4], 'name':['Andrew', 'Bobo', 'Claire', 'David']})
logins = pd.DataFrame({'log_id':[1,2,3,4], 'name':['Andrew', 'Clark', 'Claire', 'Bobo']})
print(registrations)
print(logins)
df = pd.merge(registrations, logins, how = "inner", on = "name") #inner join if key present in both tables
print(df)
print(df.isnull()) #return DF with truth values for null check
#df.dropna() drops Na rows
#df.fillna("string") fills cells with Na values with string or func param
