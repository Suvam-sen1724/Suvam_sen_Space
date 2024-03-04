"""
Question 2:
Import the data (person_details.csv) created in question 1, add two more data entities
with details of your friend and yours, and print the last five rows.

"""
import pandas  as pd
dt = pd.read_csv('person_details.csv')
dt.loc[10] = ['Tanisha','Female',21,'Bhubaneswar',4000]
dt.loc[11] = ['Suvam','Male',21,'Bhubaneswar',9000]
print(dt[7:])

"""
Answer:
       Name  Gender  Age         City  Living Expenses
7    Hannah  Female   60    San Diego             3700
8     Isaac    Male   65       Dallas             2900
9      Jack    Male   70     San Jose             3800
10  Tanisha  Female   21  Bhubaneswar             4000
11    Suvam    Male   21  Bhubaneswar             9000
"""