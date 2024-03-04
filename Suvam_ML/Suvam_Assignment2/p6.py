"""
Question 6:
A group of 8 students is forming a committee of 3 members. Write a Python program
using SciPy to calculate the total number of possible committees that can be formed.

"""
import scipy as sp

students = 8
members = 3

print("Total number of possible committees that can be formed: ",sp.special.comb(students, members))

"""
Answer:
Total number of possible committees that can be formed:  56.0
"""