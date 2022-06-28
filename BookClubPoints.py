# Starting Out With Python 5th Edition: Chapter 3 - Exercise 14

# Input number of books the user has purchased this month
books_purchased = int(input('Enter number of books purchased this month: '))

# Decision structure based on number of books purchased
if books_purchased < 2:
   print('Earned 0 points this month.')
elif (books_purchased >=2) and (books_purchased < 4):
   print('Earned 2 points this month.')
elif (books_purchased >= 4) and (books_purchased < 6):
   print('Earned 15 points this month.')
elif (books_purchased >= 6) and (books_purchased < 8):
   print('Earned 30 points this month.')
else:
   print('Earned 60 points this month.')
