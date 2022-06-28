# Starting Out With Python 5th Edition: Chapter 3 - Exercise 5

# Input an object's mass
mass = float(input('Enter an object\'s mass: '))

# Calculate weight as mass * 9.8
weight = mass * 9.8

# Decision structure
if weight > 500:
   		print('Too heavy.')
elif weight < 100:
   		print('Too light.')
else:
   		print(f'Object\'s weight is {weight:.2f} newtons.')
