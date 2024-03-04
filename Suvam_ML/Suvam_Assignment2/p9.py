"""
Question 9:
Given a dataset representing the performance scores of students in a class, Write Python
code using Matplotlib to perform the following tasks:
A. Create a bar graph showing the SML scores of each student.
B. Create a histogram showing the distribution of AD scores.
C. Create a scatter plot to visualize the relationship between SML and AD scores.
D. Create a pie chart to represent the distribution of scores across students.

| Students  |  SML_scores | AD_score  |
| Alice     |  85         | 80        |
| Bob       |  90         | 75        |
| Charlie   |  70         | 85        |
| David     |  80         | 70        |
| Emily     |  75         | 90        |
"""
import matplotlib.pyplot as plt

# Data
students = ['Alice', 'Bob', 'Charlie', 'David', 'Emily']
sml_scores = [85, 90, 70, 80, 75]

# A. Create a bar graph showing the SML scores of each student.
plt.bar(students, sml_scores, color='skyblue', edgecolor='black')
plt.xlabel('Students')
plt.ylabel('SML Scores')
plt.title('Q9A. SML Scores of Students')
plt.savefig('Q9A.png')      #Ignore this code fragment as it will just save data as img.
plt.show()

# B. Create a histogram showing the distribution of AD scores.
ad_scores = [80, 75, 85, 70, 90]

plt.hist(ad_scores, bins=10, color='salmon', edgecolor='black')
plt.xlabel('AD Scores')
plt.ylabel('Frequency')
plt.title('Q9B. Distribution of AD Scores')
plt.savefig('Q9B.png')      #Ignore this code fragment as it will just save data as img.
plt.show()

# C. Create a scatter plot to visualize the relationship between SML and AD scores.
ad_scores = [80, 75,  85, 70, 90]

plt.scatter(sml_scores, ad_scores, color='purple', marker='o')
plt.xlabel('SML Scores')
plt.ylabel('AD Scores')
plt.title('Q9C. Relationship between SML and AD Scores')
plt.savefig('Q9C.png')      #Ignore this code fragment as it will just save data as img.
plt.show()

# D. Create a pie chart to represent the distribution of scores across students.
total_scores = [165, 165, 155, 150, 165]

plt.pie(total_scores, labels=students, autopct='%1.1f%%', colors=['gold', 'lightcoral', 'lightgreen', 'lightskyblue', 'plum'])
plt.title('Q9D. Score Distribution Across Students')
plt.savefig('Q9D.png')      #Ignore this code fragment as it will just save data as img.
plt.show()
