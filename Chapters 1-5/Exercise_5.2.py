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