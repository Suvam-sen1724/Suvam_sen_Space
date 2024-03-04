"""
Question 8:
Given a company's monthly sales data (in thousands of dollars) for the past year. The data
is stored in a Python list. Write Python code using Matplotlib to create a line plot to
visualize the trend of monthly sales over the past year. Add labels to the x-axis and y-axis
with appropriate names. Add a title to the plot indicating what it represents. Save the
image in your local directory.
monthly_sales = [50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105]
(Hints: The x-axis is months [1-12], and the y-axis is monthly sales)
"""
import matplotlib.pyplot as plt

monthly_sales = [50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105]

months = range(1, 13)

plt.plot(months, monthly_sales)

plt.xlabel("Month")
plt.ylabel("Sales (in thousands of dollars)")
plt.title("Q8. Monthly Sales Over the Past Year")
plt.savefig("P8_img.png") #This part can be ignored 
plt.show()