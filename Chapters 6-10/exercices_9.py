# Exercise 1: Write a program that reads the words # in words.txt and stores them as keys in a dictionary.
# It doesn’t matter what the values are. Then you can use the in operator as a fast way to check whether 
# a string is in the dictionary

text = open('words.txt')    # The handler
dct = dict()                  # Initiate the dict
for line in text:
    words = line.split()    
    for word in words:
        dct[word] = None    # Every word is a key and has a None value
print(dct)

# Same excercise but, I'll count the repeats of every word and putting as value

text = open('mbox-short.txt')    # The handler
dct = dict()                    # Initiate the dict
for line in text:
    words = line.split()    
    for word in words:
        dct[word] = dct.get(word,0) + 1    # In this case verify if the key(word) exist and count it
print(dct)

# Exercise 2: Write a program that categorizes each mail message by which day of the week the commit was done. 
# To do this look for lines that start with “From”, then look for the third word and keep a running count of each
#  of the days of the week. At the end of the program print out the contents of your dictionary 
# (order does not matter).

fhand = input('Enter a file name: ')

try:
    text = open(fhand)                      # The handler
    dct = dict()
    for line in text:
        if not line.startswith('From '): continue # There's a tricky here with 'From ' and 'From:' so beware with th space
        words = line.split()
        if words[2] not in dct:
            dct[words[2]] = 1
        else:
            dct[words[2]] += 1
except:
    print('File cannot be opened:', fhand)
    exit()

print(dct)

# Exercise 3: Write a program to read through a mail log, build a histogram using a dictionary to count 
# how many messages have come from each email address, and print the dictionary.

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

print(dct)

# Exercise 4: Add code to the above program to figure out who has the most messages in the file. 
# After all the data has been read and the dictionary has been created, look through the dictionary 
# using a maximum loop (see Chapter 5: Maximum and minimum loops) to find who has the most messages and 
# print how many messages the person has.

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
max = None
mail = None
for key in dct: # Loop trough every key
    if max == None or dct.get(key) > max: # Getting the max value 
        max = dct.get(key)
        mail = key

print(mail, max)

# Exercise 5: This program records the domain name (instead of the address) where the message was sent from 
# instead of who the mail came from (i.e., the whole email address). At the end of the program, print out 
# the contents of your dictionary.

fhand = input('Enter a file name: ')

try:
    text = open(fhand)                      # The handler
    dct = dict()
    for line in text:
        if not line.startswith('From '): continue # There's a tricky here with 'From ' and 'From:' so beware with th space
        words = line.split()
        domain = words[1] # Creating a list that contains all the mails
        domain = domain[domain.find('@')+1:] # taking just the domains
        if domain not in dct:
            dct[domain] = 1 # Creating a dictionary with the domains and giving a value of one
        else:
            dct[domain] += 1 # Counting the domains if already exist
except:
    print('File cannot be opened:', fhand)
    exit()

print(dct)         