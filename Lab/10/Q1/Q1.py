import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('heart.csv')
plt.figure(figsize=(12,18))
plt.subplot(7,2,1)
plt.grid(visible=True)
sns.histplot(df,x='age')
plt.subplot(7,2,2)
plt.grid(visible=True)
sns.histplot(df,x='sex')
plt.subplot(7,2,3)
plt.grid(visible=True)
sns.histplot(df,x='cp')
plt.subplot(7,2,4)
plt.grid(visible=True)
sns.histplot(df,x='trestbps')
plt.subplot(7,2,5)
plt.grid(visible=True)
sns.histplot(df,x='chol')
plt.subplot(7,2,6)
plt.grid(visible=True)
sns.histplot(df,x='fbs')
plt.subplot(7,2,7)
plt.grid(visible=True)
sns.histplot(df,x='restecg')
plt.subplot(7,2,8)
plt.grid(visible=True)
sns.histplot(df,x='thalach')
plt.subplot(7,2,9)
plt.grid(visible=True)
sns.histplot(df,x='exang')
plt.subplot(7,2,10)
plt.grid(visible=True)
sns.histplot(df,x='oldpeak')
plt.subplot(7,2,11)
plt.grid(visible=True)
sns.histplot(df,x='slope')
plt.subplot(7,2,12)
plt.grid(visible=True)
sns.histplot(df,x='ca')
plt.subplot(7,2,13)
plt.grid(visible=True)
sns.histplot(df,x='thal')
plt.subplot(7,2,14)
plt.grid(visible=True)
sns.histplot(df,x='target')
plt.show()




#PAPER 2

plt.figure()
sns.histplot(data=df,x="fbs")
plt.show()

plt.figure()
sns.boxplot(x="fbs",y="age",data=df)
plt.show()

plt.figure()
sns.scatterplot(data=df,x="fbs",y="age")
plt.show()

plt.figure()
sns.lineplot(y=df["age"],x=df["fbs"])
plt.show()

plt.figure()
sns.displot(df)
plt.ylabel("fbs")
plt.show()

plt.figure()
sns.pairplot(df,hue="age")
plt.show()
