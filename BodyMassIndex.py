# Formula: BMI = weight * 703/height^2
# Input weight in pounds
weight = float(input('Enter weight in pounds: '))

# Input height in inches
height = float(input('Enter height in inches: '))

# Calculate BMI and display BMI
bmi = weight * (703/(height**2))
print(f'BMI: {bmi:.1f}')

# Display whether user has optimal weight, is underweight, or overweight
if (bmi >= 18.5) and (bmi <= 25):
   print('Your weight is optimal.')
elif bmi < 18.5:
   print('Underweight.')
else:
   print('Overweight.')