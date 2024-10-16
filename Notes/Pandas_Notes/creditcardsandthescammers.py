import pandas as pd

def last_four(num):
    return str(num)[-4:]

def yelp(price):
    if price<10:
        return '$'
    elif price >=10 and price < 30:
        return '$$'
    else:
        return '$$$'
df2 = pd.read_csv('tips.csv')
print(df2['CC Number'][0])
print(last_four(3560325168603410))
df2['last_four'] = df2['CC Number'].apply(last_four)
df2['Expensive'] = df2['total_bill'].apply(yelp)
print(df2['Expensive'])
print(df2['total_bill'].between(10,20,inclusive='both')) #prints total bill col with values between 10,20, both bounds inclusive
print(df2['price_per_person'].between(5,8,inclusive = 'both'))
print(df2.nlargest(10,'tip'))
print(df2.nsmallest(10,'tip'))
