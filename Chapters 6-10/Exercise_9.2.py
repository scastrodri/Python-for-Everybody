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