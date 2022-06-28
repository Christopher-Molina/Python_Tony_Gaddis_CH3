# Starting Out With Python 5th Edition: Chapter 3 - Exercise 3

# Input age of user
ageOfUser = int(input('Enter your age: '))

# Decision structure
if ageOfUser <= 1:
   print('Infant')
elif ageOfUser > 1 and ageOfUser < 13:
   print('Child')
elif ageOfUser >= 13 and ageOfUser < 20:
   print('Teenager')
else:
   print('Adult')

# Input number within the range 1-10
number = int(input('Enter a number in the range 1-10: '))
