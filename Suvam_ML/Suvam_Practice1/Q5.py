"""
5. Write a Python program that prompts the user to enter an integer for today’s day of the
week (Sunday is 0, Monday is 1… and Saturday is 6). Also prompt the user to enter the
number of days after today for a future day and display the future day of the week.

Here is a sample run:
Enter today's day: 1
Enter the number of days elapsed since today: 3
Today is Monday and the future day is Thursday
Enter today's day: 0
Enter the number of days elapsed since today: 31
Today is Sunday and the future day is Wednesday

"""

days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

todaysDate = int(input("Enter an integer for today's day of the week (0 - 6, whereSunday is 0 and Saturday is 6): "))

print(f"Today is {days[todaysDate]}")

daysElapsed = int(input("Enter the number of days elapsed since today: "))

if(daysElapsed<=0):
    print("Please enter valid integer values.")
else:
    futureDay = (todaysDate + daysElapsed) % 7

print(f"Today is {days[todaysDate]} and the future day is {days[futureDay]}")

    
