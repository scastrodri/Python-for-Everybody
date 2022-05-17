# Exercise 6: Rewrite your pay computation with time-and-a-half for overtime and create a function 
# called computepay which takes two parameters (hours and rate).
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

def computepay (hours, rate):
    if hours > 40:
        pay = (hours - 40) * (rate * 1.5) + (40 * rate)
    else:
        pay = hours * rate
    return print('Pay: ', pay)

computepay(hours, rate)