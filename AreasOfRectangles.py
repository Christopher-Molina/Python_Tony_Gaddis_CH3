# Starting Out With Python 5th Edition: Chapter 3 - Exercise 2

# Input length of rectangle one
rectangle1_length = float(input('Enter length of rectangle one: '))

# Input width of rectangle one
rectangle1_width = float(input('Enter width of rectangle one: '))

# Calculate area as length * width for rectangle one
rectangle1_area = rectangle1_length * rectangle1_width

# Input length of rectangle two
rectangle2_length = float(input('Enter length of rectangle two: '))

# Input width of rectangle two
rectangle2_width = float(input('Enter width of rectangle two: '))

# Calculate area as length * width for rectangle two
rectangle2_area = rectangle2_length * rectangle2_width

# Decision structure
if rectangle1_area == rectangle2_area:
   print('Both rectangles have the same area')
elif rectangle1_area < rectangle2_area:
   print('Rectangle two has a greater area')
else:
   print('Rectangle one has a greater area')
