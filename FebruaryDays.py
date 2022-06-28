# Starting Out With Python 5th Edition: Chapter 3 - Exercise 16

# Input year
year = int(input('Enter a year: '))

# Determine whether year is leap year or not
if (year % 100 == 0) and (year % 400 == 0):
   leapYear = True
elif (year % 100 != 0) and (year % 4 == 0):
   leapYear = True
else:
   leapYear = False

# Display amount of days in February during the specified year
if leapYear:
   print(f'In {year} February has 29 days.')
else:
   print(f'In {year} February has 28 days.')
