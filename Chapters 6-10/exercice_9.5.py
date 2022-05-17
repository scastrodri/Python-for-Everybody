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