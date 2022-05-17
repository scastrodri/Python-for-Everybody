# Exercise 2: Rewrite your pay program using try and except so that your program handles non-numeric input 
# gracefully by printing a message and exiting the program. 
hours = input('Enter hours: ')
try: # the insurance policy to notice if the input was an integer or not
    hours = float(hours)
except:
    print('Error, please enter numeric input')
    raise SystemExit # A way to exit the program
rate = input('Enter rate: ')
try:
    rate = float(rate)
except:
    print('Error, please enter numeric input')
    exit() # another way to finish could be 'quit()'.
if hours > 40:
    print('Pay: ',(hours - 40) * (rate * 1.5) + (40 * rate))
else:
    print('Pay: ', hours * rate)