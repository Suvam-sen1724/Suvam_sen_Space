"""
7. Write a Python program that prompts the user to enter the month and year and displays
the number of days in the month. For example, if the user entered month 2 and year 2012,
the program should display that February 2012 had 29 days. If the user entered month 3
and year 2015, the program should display that March 2015 had 31 days.
"""
import calendar


month = int(input("Enter the month (1-12): "))
year = int(input("Enter the year: "))

if month == 2:
    # February: Check for leap year
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"February {year} had 29 days.")
    else:
        print(f"February {year} had 28 days.")
elif month in [4, 6, 9, 11]:
    # April, June, September, November: 30 days
    print(f"{calendar.month_name[month]} {year} had 30 days.")
elif month in [1, 3, 5, 7, 8, 10, 12]:
    # January, March, May, July, August, October, December: 31 days
    print(f"{calendar.month_name[month]} {year} had 31 days.")
else:
    print("Invalid month. Please enter a valid month (1-12).")
