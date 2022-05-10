# Exercise 1: Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.
hours = float(input('Enter hours: '))
rate = float(input('Enter rate: '))
if hours > 40:
    print('Pay: ',(hours - 40) * (rate * 1.5) + (40 * rate))
else:
    print('Pay: ', hours * rate)

# Exercise 2: Rewrite your pay program using try and except so that your program handles non-numeric input 
# gracefully by printing a message and exiting the program. 
hours = input('Enter hours: ')
try:
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

# Exercise 3: Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, 
# print an error message. If the score is between 0.0 and 1.0, print a grade using the following table:
'''
Score Grade
>= 0.9 A
>= 0.8 B
>= 0.7 C
>= 0.6 D
< 0.6 F
'''
score = input('Enter score: ')
try:
    score = float(score)
except:
    print('Bad score')
    raise SystemExit
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