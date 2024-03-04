"""
2. Write a Python program to input the mark of a student and check if the student mark is
greater than or equal to 40, then it generates the following message.
“Congratulation! You have passed the exam.”
Otherwise the output message is
“Sorry! You have failed the exam.”
"""

a = int(input("Enter your marks: "))
if(a>=40):
    print("\"Congratulations, you have successfully passed the Exam\"")
else:
    print("\"Sorry, you have failed the Exam\"")