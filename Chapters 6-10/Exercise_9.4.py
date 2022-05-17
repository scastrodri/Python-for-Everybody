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