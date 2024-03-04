"""
Question 9:
Write a Python program that reads an integer between 0 and 1000 and adds all the digits in the integer. 
For example, if an integer is 749, the sum of all its digits is 20. 
Hint: Use the % operator to extract digits and the / operator to remove the extracted digit. 
For instance, 749 % 10 = 9 and 749 / 10 = 74. 
Here is a sample run: Enter a number between 0 and 1000: 999 The sum of the digits is 27

code:
"""
a = int(input("Enter a number: "))
if a>=0 and a<=1000:
    sum = 0
    while a > 0:
        sum += a%10
        a //= 10
    print("The sum of the digits is", sum)
else:
    print("Enter a number between 0 and 1000")

"""
Answer:
Enter a number: 798
The sum of the digits is 24

Enter a number: 1099
Enter a number between 0 and 1000
"""