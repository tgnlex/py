import pandas as pd 

d = {'col1' : [1, 2, 3, 4, 7], 'col2': [4, 5, 6, 9, 5], 'col3': [7, 8, 9, 12, 1, 11]}
df = pd.DataFrame(data=d)

count_column = df.shape[1]
count_row = df.shape[0]

print(count_column)
print(count_row)
print(df)

