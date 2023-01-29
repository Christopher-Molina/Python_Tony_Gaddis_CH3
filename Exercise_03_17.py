# Starting Out With Python 5th Edition: Chapter 3 - Exercise 17

reply = ''
print('Reboot the computer and try to connect.')
reply = input('Did that fix the problem? ').lower()

if (reply == 'yes') or (reply == 'no'):
   if reply == 'yes':
       print('\nHave a great day!')
   elif reply == 'no':
       print('\nReboot the router and try to connect')
       reply = input('Did that fix the problem? ').lower()
       if (reply == 'yes') or (reply == 'no'):
           if reply == 'yes':
               print('\nHave a great day!')
           elif reply == 'no':
               print('\nMake sure the cables between the router and & modem are plugged in firmly.')
               reply = input('Did that fix the problem? ').lower()
               if (reply == 'yes') or (reply == 'no'):
                   if reply == 'yes':
                       print('\nHave a great day!')
                   elif reply == 'no':
                       print('\nMove the router to a new location and try to connect.')
                       reply = input('Did that fix the problem? ').lower()
                       if (reply == 'yes') or (reply == 'no'):
                           if reply == 'yes':
                               print('\nHave a great day!')
                           else:
                               print('\nGet a new router.')
                       else:
                           print('\nPlease enter "Yes" or "No". Rerun the program and try again.')
       else:
           print('\nPlease enter "Yes" or "No". Rerun the program and try again.')
else:
   print('\nPlease enter "Yes" or "No". Rerun the program and try again.')
