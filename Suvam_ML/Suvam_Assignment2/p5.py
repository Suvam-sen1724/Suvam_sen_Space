"""
Question 5:
Given the heights (in inches) of two groups of students, Group A and Group B. Write a
Python program to determine the difference in the mean heights between the two groups.
group_a_heights = [65, 68, 70, 72, 64, 67, 71, 66, 68, 69]
group_b_heights = [62, 64, 67, 68, 63, 65, 66, 61, 64, 67]

"""

import numpy as np

group_a_heights = [65, 68, 70, 72, 64, 67, 71, 66, 68, 69]
group_b_heights = [62, 64, 67, 68, 63, 65, 66, 61, 64, 67]

group_a_mean = np.mean(group_a_heights)
group_b_mean = np.mean(group_b_heights)

difference = group_a_mean - group_b_mean
print("Difference between the two groups is ",difference)

"""
Answer:
Difference between the two groups is  3.299999999999997
"""