# Starting Out With Python 5th Edition: Chapter 3 - Exercise 8

import math

# Constants for count of each package
DOGS_PACK = 10
BUNS_PACK = 8

# Input number of people attending the cookout
number_of_people = int(input('Enter number of people attending the cookout: '))

# Input number of hot dogs each person will be given
number_of_hot_dogs = int(input('Enter number of hot dogs each person will be given: '))

# Calculate and display the minimum number of hot dog packages required
dog_packages_required = math.ceil(number_of_people * number_of_hot_dogs / DOGS_PACK)
print('Hot dog packages required', dog_packages_required)

# Calculate and display the minimum number of hot dog bun packages required
bun_packages_required = math.ceil(number_of_people * number_of_hot_dogs / BUNS_PACK)
print('Hot dog buns packages required', bun_packages_required)

# Calculate and display number of hot dogs that will be left over
hot_dogs_leftover = (dog_packages_required * DOGS_PACK) - (number_of_people * number_of_hot_dogs)
print('Hot dog packages leftover', abs(hot_dogs_leftover))

# Calculate and display the number of hot dog buns that will be left over
buns_leftover = (bun_packages_required * BUNS_PACK) - (number_of_people * number_of_hot_dogs)
print('Hot dog buns packages leftover', abs(buns_leftover))