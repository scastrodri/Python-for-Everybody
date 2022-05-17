# Exercise 3: Use urllib to replicate the previous exercise of (1) retrieving the document from a URL, 
# (2) displaying up to 3000 characters, and (3) counting the overall number of characters in the document. 
# Don’t worry about the headers for this exercise, simply show the first 3000 characters of the document contents.

import urllib.request

url = input('Please enter a url: ') # Prompt the user for the URL
count = 0
try:
    fhand = urllib.request.urlopen(url) # Handler to the url
    fhand = fhand.read().decode().replace(' ','')[:3001] # Reading, decoding, replacing the whitespaces (just for fun) and taking the first 3000 characters.
except:
    print('The url: ' + url + ' is not valid')
    exit()
print(fhand)