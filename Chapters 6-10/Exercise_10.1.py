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