"""
6. Write a Python program that prompts the user to enter three integers and display the
integers in non-decreasing order.
Here is a sample run:
Enter three integers: 2 4 3
Display the integers in non-decreasing order:
2 3 4
"""

numbers_list = []
for i in range(0,3):
    numbers_list.append(input("Enter three integers (separated by spaces): "))

numbers_list.sort()

print("Display the integers in non-decreasing order:")
print(*numbers_list)
