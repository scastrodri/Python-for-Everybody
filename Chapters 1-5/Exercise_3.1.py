# Exercise 1: Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.
hours = float(input('Enter hours: '))
rate = float(input('Enter rate: '))
if hours > 40:
    print('Pay: ',(hours - 40) * (rate * 1.5) + (40 * rate))
else:
    print('Pay: ', hours * rate)