# Starting Out With Python 5th Edition: Chapter 3 - Exercise 7
# Input primary color one
color_one = input('Enter primary color one: ').lower()

# Input primary color two
color_two = input('Enter primary color two: ').lower()

# Display secondary color formed by the primary colors inputted by user
if (color_one == 'red' and color_two == 'blue') or (color_one == 'blue' and color_two == 'red'):
   		print('Red and blue make purple.')
elif (color_one == 'red' and color_two == 'yellow') or (color_one == 'yellow' and color_two == 'red'):
   		print('Red and yellow make orange.')
elif (color_one == 'blue' and color_two == 'yellow') or (color_one == 'yellow' and color_two == 'blue'):
   		print('Blue and yellow make green.')
else:
   		print('Error, make sure to enter a primary color (red, blue, or yellow)')
