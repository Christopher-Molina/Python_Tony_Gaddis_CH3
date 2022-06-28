# Starting Out With Python 5th Edition: Chapter 3 - Exercise 10

# Define constants for a value of a penny, nickel, dime, and quarter
PENNY = 0.01
NICKEL = 0.05
DIME = 0.10
QUARTER = 0.25

# Input number of pennies
number_of_pennies = int(input('Enter number of pennies: '))

# Input number of nickels
number_of_nickels = int(input('Enter number of nickles: '))

# Input number of dimes
number_of_dimes = int(input('Enter number of dimes: '))

# Input number of quarters
number_of_quarters = int(input('Enter number of quarters: '))

# Calculate total value
total_value = (number_of_pennies * PENNY) + (number_of_nickels * NICKEL) \
             + (number_of_dimes * DIME) + (number_of_quarters * QUARTER)

# Decision structure
if total_value == 1:
   print('\nCongratulations, the amount entered is equal to $1')
else:
   print('\nThe amount entered, does not equal to $1')
