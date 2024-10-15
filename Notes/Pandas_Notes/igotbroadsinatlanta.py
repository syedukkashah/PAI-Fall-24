#playing around with dataframes using pandas 
import pandas as pd
df = pd.read_csv("heart.csv")
df['sex'] = df['sex'].replace({1:'male', 0:'female'})
print(df['sex'].head(10))
print(df.columns)
df.columns = ['age', 'sex', 'chest_pain_type', 'resting_blood_pressure', 'cholesterol', 'fasting_blood_sugar', 'rest_ecg',
              'max_heart_rate_achieved', 'exercise_induced_angina', 'st_depression', 'st_slope', 'num_major_vessels',
               'thalassemia', 'target']
df['chest_pain_type'] = df['chest_pain_type'].replace({0:'typical angina', 1:'atypical angina', 2:'non-anginal pain', 3:'asymptomatic'})
df['fasting_blood_sugar'] = df['fasting_blood_sugar'].replace({0:'lower than 120mg/ml', 1:'greater than 120mg/ml'})
df['rest_ecg'] = df['rest_ecg'].replace({0:'normal', 1:'ST-T wave abnormality', 2:'left ventricular hypertrophy'})
df['exercise_induced_angina'] = df['exercise_induced_angina'].replace({0:'no', 1:'yes'})
df['st_slope'] = df['st_slope'].replace({1:'upsloping', 2:'flat', 3:'downsloping'})
df['thalassemia'] = df['thalassemia'].replace({1:'normal', 2:'fixed defect', 3:'reversable defect'})
print(df.head(10))
df = df.rename(columns = {'rest_ecg':'ecg', 'sex':'gender'}) #for renaming the columns
df = df.rename(columns = {'age':"AGE"})
df = df.rename(columns = {'chest_pain_type':'Chest pain type'})
print(df.head())
print(df.describe())#returns info about data frame
#inserting columns
df = pd.read_csv("heart.csv") #reloading original file
df = df.head(10) #we resize the data frame by init it to first 10 rows since the list we use for inserting the names will be of size 10
Names = ['Ali', 'Salman', 'Sohail', 'Mohsin', 'Waqas', 'Zeshan', 'Babar', 'John', 'Elon', 'Michael']
df.insert(0,'name', Names) #(position(loc), column name, column data(a list)
print(df.head())
df = df.head() #resize to first 5 rows
df = df[['age', 'sex', 'cp', 'target']] #now the data frame only has columns mentioned
print(df)

#dropping cols
target_data = df['target'] #init target col to a target_data list
df.drop(labels = ['target'], axis=1, inplace=True) #inplace = True changes the original dataframe while inplace=False makes the copy
print(df)
df.insert(3, 'target', target_data) #inserting target back into the data frame
print(df)
cp_data = df['cp']
df_copy = df.drop(labels = ['cp'], axis = 1, inplace = False)
print(df) #since inplace=False when df.drop() was used, df will still have cp col
print(df_copy) #df_copy will not have the cp col
df.drop(labels = ['cp'], axis = 1, inplace = True) #the cp col will now be removed from the og df since inplace = True
print(df)
df.insert(2,'cp', cp_data) #inserting cp back into the og df
print(df)

#adding rows
new_row = {'age':25, 'sex':1, 'cp':3, 'target':0}
df.loc[df.index.size - 1] = new_row #df.index.size = 5, so new_row will be added at index#4
#ignore_index is False by default, if True, index values are not used along concatenation axis
#and the resulting axis will be labeled 0,1....,n-1, can't append dictionary if ignore_index = False
print(df)

#adding rows at a specific index
df.loc[2] = [49, 0, 2, 0] #the existing row at index 2 will be replaced
print(df)

#dropping rows
df = df.drop(labels = [2,3], axis = 'rows') #the df will now have indexes 0,1,4
print(df)
new_row = [{'age':49, 'sex':0, 'cp':2, 'target':0}, {'age':61, 'sex':1, 'cp':0, 'target':0}]
df.loc[df.index.size - 1] =new_row[0] #df.index.size = 3, so new_row will be added as index#2
print(df) #df now has indexes 0,1,4,2

#to reset indexes from 0-4, we will use reset_index
df.reset_index(drop = True, inplace=True)
print(df) #indexes are now 0,1,2,3

