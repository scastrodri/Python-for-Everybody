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