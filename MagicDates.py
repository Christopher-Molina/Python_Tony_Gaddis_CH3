# Starting Out With Python 5th Edition: Chapter 3 - Exercise 6

# Input day
day = int(input('Enter a day of the month: '))

# Input month
month = int(input('Enter a month in numeric format (1-12): '))

# Input two-digit year
year = int(input('Enter the year in two-digit format: '))

# Decision structure
if (day * month) == year:
 	  print(f'The date {day}/{month}/{year} is a magic date.')
else:
  	  print(f'The date {day}/{month}/{year} is not a magic date.')
