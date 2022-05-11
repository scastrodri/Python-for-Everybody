#Exercise 1: Write a function called chop that takes a list and modifies it, removing the first and last elements, 
# and returns None. Then write a function called middle that takes a list and returns a new list that contains 
# all but the first and last elements.

def chop(nums):
    del nums[0]
    del nums[len(nums)-1]
    return None

def middle(nums):
    return chop(nums)

nums = [3, 41, 12, 9, 74, 15, 2, 3, 4, 5]
middle(nums)
print(nums)

# Exercise 4: Find all unique words in the file romeo.txt and read it line by line. For each line, 
# split the line into a list of words using the split function. For each word, check to see if the word 
# is already in the list of unique words. If the word is not in the list of unique words, add it to the list.
# When the program completes, sort and print the list of unique words in alphabetical order.

lst = open('romeo.txt').read().split() # Reading the file and split to create a list of words
uniques = []
for word in lst: # For each word in the list
    if word not in uniques: # Check to see if the word is already in the list of unique words
        uniques.append(word) #  If the word is not in the list of unique words, add it to the list
uniques.sort() # Sort and print
print(uniques)

# Exercise 5: Minimalist Email Client. Write a program to read through the mail box data and when you find 
# line that starts with “From”, you will split the line into words using the split function. You will parse 
# the From line and print out the second word for each From line, then you will also count the number of From 
# (not From:) lines and print out a count at the end.

try:
    fhand = open(input('Enter a file name: '))
    lst = []
    count = 0
    for line in fhand:
        if not line.startswith("From:"): continue
        lst = line.split()
        count = count + 1
        print(lst[1])
    print('There were ', count , ' lines in the file with From as the first word')
except:
    print('Please enter a valid file')

# Exercise 6: Rewrite the program that prompts the user for a list of numbers and prints out the maximum 
# and minimum of the numbers at the end when the user enters “done”. Write the program to store the numbers 
# the user enters in a list and use the max() and min() functions to compute the maximum and minimum numbers 
# after the loop completes.

numbers = []
while True:
    num = input('Enter a number: ')
    if num == 'done':
        break
    try:
        numbers.append(float(num))
    except:
        print('Invalid input')
    
print('Maximum: ', max(numbers))
print('Minimum: ', min(numbers))