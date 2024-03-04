"""
4. If the ages of Rahul, Ayush and Ajay are input through the keyboard, write a Python program
to determine the elder among them.
"""

a = int(input("Enter Rahul's age: "))
b = int(input("Enter AJAY's age: "))
c = int(input("Enter ayush's age: "))

if(a>b):
    if(a>c):
        print("Rahul is the Oldest")
elif(b>c):
    print("Ajay is the Oldest")
else:
    print("Ayush is the Oldest")