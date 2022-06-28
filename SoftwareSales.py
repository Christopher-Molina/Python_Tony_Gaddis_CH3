# Starting Out With Python 5th Edition: Chapter 3 - Exercise 12

# Define constant for amount of software package
SOFTWARE_PACKAGE = 99

# Display quantity discounts table
print('Quantity\tDiscount')
print('10-19\t\t10%')
print('20-49\t\t20%')
print('50-99\t\t30%')
print('100+ \t\t10%')

# Input number of packages purchased
packages_purchased = int(input('\nEnter number of packages purchased: '))

# Decision structure based on quantity purchased
if packages_purchased < 10:
   print('\nTotal Amount: $', SOFTWARE_PACKAGE, sep='')
elif (packages_purchased >= 10) and (packages_purchased <= 19):
   discount = SOFTWARE_PACKAGE * 0.10
   print(f'\nDiscount: ${discount:.2f}')
   print(f'Total Amount: ${SOFTWARE_PACKAGE - discount:.2f}')
elif (packages_purchased >= 20) and (packages_purchased <= 49):
   discount = SOFTWARE_PACKAGE * 0.20
   print(f'\nDiscount: ${discount:.2f}')
   print(f'Total Amount: ${SOFTWARE_PACKAGE - discount:.2f}')
elif (packages_purchased >= 50) and (packages_purchased <= 99):
   discount = SOFTWARE_PACKAGE * 0.30
   print(f'\nDiscount: ${discount:.2f}')
   print(f'Total Amount: ${SOFTWARE_PACKAGE - discount:.2f}')
else:
   discount = SOFTWARE_PACKAGE * 0.40
   print(f'\nDiscount: ${discount:.2f}')
   print(f'Total Amount: ${SOFTWARE_PACKAGE - discount:.2f}')