"""
Question 1:
Evaluate the following expressions involving arithmetic operators:
a. -7*20+8/16*2+54
b. 7**2//9%3
c. (7-4*2)*10-25*8//5
d. 5%10+10-25*8//5
e. ’hello’*2-5

Code:
"""
print(-7*20+8/16*2+54)
print(7**2//9%3)
print((7-4*2)*10-25*8//5)
print(5%10+10-25*8//5)
print('hello'*2-5)

"""
Answer:
-85.0
2
-50
-25
Traceback (most recent call last):
  File "e:\Suvam_ML\Assignment1\P1.py", line 6, in <module>  
    print('hello'*2-5)
          ~~~~~~~~~^~
TypeError: unsupported operand type(s) for -: 'str' and 'int'
"""