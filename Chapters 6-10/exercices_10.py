# Exercise 1: Revise a previous program as follows: Read and parse the “From” lines and pull out the addresses 
# from the line. Count the number of messages from each person using a dictionary. After all the data has been 
# read, print the person with the most commits by creating a list of (count, email) tuples from the dictionary. 
# Then sort the list in reverse order and print out the person who has the most commits.

fhand = input('Enter a file name: ')

try:
    text = open(fhand)                      # The handler
    dct = dict()
    for line in text:
        if not line.startswith('From '): continue # There's a tricky here with 'From ' and 'From:' so beware with th space
        words = line.split()
        if words[1] not in dct:
            dct[words[1]] = 1
        else:
            dct[words[1]] += 1
except:
    print('File cannot be opened:', fhand)
    exit()

lst = list()
for key,value in list(dct.items()): # Loop the element's dictionary
    lst.append((value,key)) # Adding the values and keys to the list
lst.sort(reverse=True) # Sorting from biggest to smallest

max = None
email = None
for value, key in lst: # Loop the list
    if max == None or value > max: # Checking the biggest value to assing as the answer
        max = value
        email = key

print(email, max)

# Exercise 2: This program counts the distribution of the hour of the day for each of the messages. 
# You can pull the hour from the “From” line by finding the time string and then splitting that string 
# into parts using the colon character. Once you have accumulated the counts for each hour, print out the counts, 
# one per line, sorted by hour.
fhand = input('Enter a file name: ')

try:
    text = open(fhand)                      # The handler
    dct = dict()
    for line in text:
        if not line.startswith('From '): continue # There's a tricky here with 'From ' and 'From:' so beware with th space
        words = line.split()
        hour = words[5].split(':') # The time is in the sixth position of the line, then separate to get the hour
        if hour[0] not in dct: # Creating a dictionary with the hour and giving a value of one
            dct[hour[0]] = 1
        else:
            dct[hour[0]] += 1 # Counting the hour if already exist
except:
    print('File cannot be opened:', fhand)
    exit()

lst = sorted(tuple(dct.items())) # Create a list from a tupple from the dictionary's item and sorted by the key(hour)
for hour, cant in lst: # Loop the list and printin one by one element
    print(hour,cant)

# Exercise 3: Write a program that reads a file and prints the letters in decreasing order of frequency. 
# Your program should convert all the input to lower case and only count the letters a-z. Your program should 
# not count spaces, digits, punctuation, or anything other than the letters a-z. Find text samples from several 
# different languages and see how letter frequency varies between languages. Compare your results with the tables
# at https://wikipedia.org/wiki/Letter_frequencies

import string # for this excersise I'm going to use string.punctuation, string.digits, translate and maketranslate

dct = dict()
lst = list()
count = 0

fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

for line in fhand:
    line = line.rstrip()
    # A explanation here: The string.punctuation is a string with the characters: !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
    # In this case maketrans has three parameter, the first is what we want to change, the second with what do we
    # want to change, and the third what is a string that we want to remove.
    # If we just use the maketrans method it will return a dict with the letters in ascii so we use translate method
    # to convert that ascii in text
    line = line.translate(line.maketrans('', '', string.punctuation + string.digits + ' ')).lower()
    for words in line:
        for letter in words:
            count += 1 # To count the amount of letters
            if letter not in dct:
                dct[letter] = 1
            else:
                dct[letter] += 1

for key, value in list(dct.items()): # Loop a lis with the letters and its amounts
    lst.append((value,key))
lst.sort(reverse=True)
for cant, letter in lst:
    print(letter, round(100*float(cant)/count,3),'%')