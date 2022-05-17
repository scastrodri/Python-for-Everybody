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