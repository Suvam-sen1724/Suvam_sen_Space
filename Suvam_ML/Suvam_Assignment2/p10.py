"""
Question 10:
A dataset containing information about a company's monthly sales revenue (in thousands
of dollars) for the past year, along with the corresponding months. Write Python code
using Seaborn to create a line plot to visualize the trend of monthly sales revenue over the
past year.
data = {
'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
'Sales_Revenue': [50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105]
}
"""

import seaborn as sns
import matplotlib.pyplot as plt

# Data
data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    'Sales_Revenue': [50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105]
}

sns.set(style="darkgrid")   #Ignore this code as it will set the background color
plt.figure(figsize=(16,9))  #Ignore this code as it will just resize the figure

sns.lineplot(x='Month', y='Sales_Revenue', data=data, marker='o', color='b')
plt.xlabel('Month')
plt.ylabel('Sales Revenue (in thousands of $)')
plt.title('Q10. Monthly Sales Revenue Trend')
plt.savefig('Q10.png')      #Ignore this code as it will save the file as image
plt.show()

