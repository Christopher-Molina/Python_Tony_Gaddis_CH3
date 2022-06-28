# Starting Out With Python 5th Edition: Chapter 3 - Exercise 13

# Display shipping charges table
print('Weight of Package                        Rate Per Pound')
print('2 Pounds or Less                                  $1.50')
print('Over 2 Pounds, Not More than 6 Pounds             $3.00')
print('Over 6 Pounds, Not More than 10 Pounds            $4.00')
print('Over 10 Pounds                                    $4.75\n')

# Input weight of the package
weight_of_package = int(input('Enter weight of the package: '))

# Calculate rate per pound
if weight_of_package <= 2:
   rate_per_pound = 1.50
elif (weight_of_package > 2) and (weight_of_package <= 6):
   rate_per_pound = 3.00
elif (weight_of_package > 6) and (weight_of_package <= 10):
   rate_per_pound = 4.00
else:
   rate_per_pound = 4.75

# Calculate and display shipping charges
print(f'Shipping Cost: ${weight_of_package * rate_per_pound:.2f}')