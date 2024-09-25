import pandas as pd
my_data = {
    'title': ['Movie A', 'Movie B', 'Movie C', 'Movie D'],
    'revenue': [2.5, 1.5, 3.0, 0.5],  # in millions
    'budget': [0.5, 1.2, 0.8, 0.3]    # in millions
}
df = pd.DataFrame(data=my_data)
print(df[(df['revenue'] > 2) & (df['budget'] < 1)])
