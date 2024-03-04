"""
Question 3:
Import the data (person_details.csv) and perform the following tasks
A. Use iloc to select the first three rows and the first two columns of the DataFrame.
B. Use loc to select all the data of individuals whose living expenses are greater than
3500.
C. Use loc to select the names and ages of individuals who are females and live in
either New York or Los Angeles.
D. Use iloc to select the rows from index 2 to index 7 (inclusive) and all columns

"""
import pandas as pd
dt = pd.read_csv('person_details.csv')
dt_a = dt.iloc[[0,1,2], [0,1]]
print(dt_a,'\n')

dt_b = dt.loc[dt['Living Expenses'] > 3500]
print(dt_b,'\n')

dt_c = dt.loc[(dt['Gender'] == 'Female') & (dt['City'].isin(['New York', 'Los Angeles'])),['Name','Age']]
print(dt_c, '\n')

print(dt.iloc[2:8])

"""
Answer:

A.
      Name  Gender
0    Alice  Female
1      Bob    Male
2  Charlie    Male

B.
     Name  Gender  Age       City  Living Expenses
4   Emily  Female   45    Phoenix             4000
7  Hannah  Female   60  San Diego             3700
9    Jack    Male   70   San Jose             3800

C.
    Name  Age
0  Alice   25

D.
      Name  Gender  Age          City  Living Expenses
2  Charlie    Male   35       Chicago             3200
3    David    Male   40       Houston             2800
4    Emily  Female   45       Phoenix             4000
5    Frank    Male   50  Philadelphia             3300
6    Grace  Female   55   San Antonio             3100
7   Hannah  Female   60     San Diego             3700
"""