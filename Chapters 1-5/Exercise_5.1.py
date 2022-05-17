# Exercise 1: Write a program which repeatedly reads numbers until the user enters “done”. Once “done” is entered, 
# print out the total, count, and average of the numbers. If the user enters anything other than a number, 
# detect their mistake using try and except and print an error message and skip to the next number

number = 0
count = 0

while True:
    temp = input ('Enter a number: ')
    try:
        number = number + float(temp)
        count = count +1
    except:
        print('Invalid input')
    if temp == 'done':
        break
print(number, count, number/count)