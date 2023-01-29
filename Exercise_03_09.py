# Starting Out With Python 5th Edition: Chapter 3 - Exercise 9

print('Roulette Wheel Color\n')

# Input a number in the range 1-36
number = int(input('Enter a number in the range 1-36: '))

if number == 0:
   print('Pocket is Green')
elif (number >= 1) and (number <= 10):
   if number % 2 != 0:
       print('Pocket is Red')
   else:
       print('Pocket is Black')
elif (number >= 11) and (number <= 18):
   if number % 2 != 0:
       print('Pocket is Black')
   else:
       print('Pocket is Red')
elif (number >= 19) and (number <= 28):
   if number % 2 != 0:
       print('Pocket is Red')
   else:
       print('Pocket is Black')
elif (number >= 29) and (number <= 36):
   if number % 2 != 0:
       print('Pocket is Black')
   else:
       print('Pocket is Red')
else:
   print('Error, enter a valid number in the range 1-36')
