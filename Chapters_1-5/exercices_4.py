# Exercise 1: Run the program on your system and see what numbers you get. Run the program more than once 
# and see what numbers you get.
import random
t = [4,6,7,8,92,12,34,543]
print(random.choice(t)) # It will choice a random number from t sequence

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

# Exercise 7: Rewrite the grade program from the previous chapter using a function called 
# computegrade that takes a score as its parameter and returns a grade as a string.

score = input('Enter score: ')
try:
    score = float(score)
except:
    print('Bad score')
    raise SystemExit

def computegrade (score):
    if score >= 0 and score <= 1.0:
        if score >= 0.9: 
            print('A')
        elif score >= 0.8:
            print('B')
        elif score >= 0.7:
            print('C')
        elif score >= 0.6:
            print('D')
        else:
            print('F')
    else:
        print('Bad score')
        raise SystemExit

computegrade(score)