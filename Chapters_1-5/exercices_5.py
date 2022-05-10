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

# Exercise 2: Write another program that prompts for a list of numbers as above and at the end 
# prints out both the maximum and minimum of the numbers instead of the average.

number = 0
count = 0
largest = None
smallest = None

while True:
    temp = input ('Enter a number: ')
    try:
        temp = float(temp)
        number = number + temp
        count = count +1
        if largest == None or temp > largest:
            largest = temp
        if smallest == None or temp < smallest:
            smallest = temp
    except:
        print('Invalid input')
    if temp == 'done':
        break
print(number, count, largest, smallest)