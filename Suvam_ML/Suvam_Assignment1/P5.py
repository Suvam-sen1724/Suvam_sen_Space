"""
Question 5:
Write a Python program that takes two numbers as input parameters and returns their greatest common divisor.

code:
"""

a, b = 40, 60
print(f"The greatest common divisor of ",a," and ",b," is:")
while a:
    a, b = b % a, a

print(b)

"""
Answer:
The greatest common divisor of  40  and  60  is:
20
"""