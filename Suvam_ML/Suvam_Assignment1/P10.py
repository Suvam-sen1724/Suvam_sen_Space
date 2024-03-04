"""
Question 10:
Write a Python program to enter the first number and second number. Display the prime number between the first and second numbers.
Example:
Enter the first number: 5x
Enter the second number: 15
Expected output: 5 7 11 13

code:

"""

int1 = int(input("Enter first number: "))
int2 = int(input("Enter second number: "))
l1 = []
for num in range(int1, int2+1):
    if num > 1:
        
        for i in range(3, int(num/2)+1):
            if(num == int1 or num == int2):
                break
            if num %i ==0:
                break
            
            else:
                l1.append(num)
                break
print(l1)

"""
Answer:
Enter first number: 5
Enter second number: 15

[7, 8, 10, 11, 13, 14]

"""