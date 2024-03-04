"""
Question 1:
Create Dataframes using pandas using the given dictionary. The data name should be
person_details.csv. Save the data in your local directory and print the first five data
entities (rows).
data = {
'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emily', 'Frank', 'Grace', 'Hannah', 'Isaac', 'Jack'],
'Gender': ['Female', 'Male', 'Male', 'Male', 'Female', 'Male', 'Female', 'Female', 'Male', 'Male'],
'Age': [25, 30, 35, 40, 45, 50, 55, 60, 65, 70],
'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia', 'San Antonio',
'San Diego', 'Dallas', 'San Jose'],
'Living Expenses': [3000, 3500, 3200, 2800, 4000, 3300, 3100, 3700, 2900, 3800]
}

"""

import pandas as pd
data = {
'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emily', 'Frank', 'Grace', 'Hannah', 'Isaac', 'Jack'], 'Gender': ['Female', 'Male', 'Male', 'Male', 'Female', 'Male', 'Female', 'Female', 'Male', 'Male'], 'Age': [25, 30, 35, 40, 45, 50, 55, 60, 65, 70], 'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia', 'San Antonio', 'San Diego', 'Dallas', 'San Jose'], 'Living Expenses': [3000, 3500, 3200, 2800, 4000, 3300, 3100, 3700, 2900, 3800] 
}

df = pd.DataFrame(data)
df.to_csv('person_details.csv',index=False)

dt = pd.read_csv('person_details.csv')

print(dt[0:5])

"""
Answer:
      Name  Gender  Age         City  Living Expenses
0    Alice  Female   25     New York             3000
1      Bob    Male   30  Los Angeles             3500
2  Charlie    Male   35      Chicago             3200
3    David    Male   40      Houston             2800
4    Emily  Female   45      Phoenix             4000
"""