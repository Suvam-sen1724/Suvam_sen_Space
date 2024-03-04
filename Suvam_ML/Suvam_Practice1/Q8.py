"""
8. A University conducts a 100 mark exam for its student and grades them as follows.
Assigns a grade based on the value of the marks. Write a Python program to print the
grade according to the mark secured by the student.
| Mark Range   |     Letter Grade   |
| >=90         |     O              |
| >=80 AND <90 |     A              |
| >=70 AND <80 |     B              |
| >=60 AND <70 |     C              |
| >=50 AND <60 |     D              |
| >=40 AND <50 |     E              |
| <40          |     F              |
"""
marks = int(input("Enter your exam marks (out of 100): "))
print("Your exam marks grade is: ")
if marks >= 90:
    print("O")
elif marks >= 80:
    print("A")
elif marks >= 70:
    print("B")
elif marks >= 60:
    print("C")
elif marks >= 50:
    print("D")
elif marks >= 40:
    print("E")
else:
    print("F")



