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