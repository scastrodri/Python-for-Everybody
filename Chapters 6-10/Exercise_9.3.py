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