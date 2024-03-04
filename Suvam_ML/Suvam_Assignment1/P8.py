"""
 Question 8:
An integer n is divisible by 9 if the sum of its digits is divisible by 9. Use this concept in your program to determine whether or not the number is divisible by 9. Use while loop.

Test it on the following number: 
n = 154368
Hint: Use the % operator to get each digit, then use the / operator to remove the digit. 
Sample run 1: Enter a number: 154368 The number 154368 is divisible by 9. 

 """

n = int(input("Enter a number: "))
num = n
sum = 0
while n > 0:
    sum += n%10
    n //= 10        # Here we divide n with // for getting integer division

if sum % 9 == 0:
    print("The number", num, "is divisible by 9.")
else:
    print("The number", num, "is not divisible by 9.")

"""
Answer:
Enter a number: 154368
The number 154368 is divisible by 9.
"""