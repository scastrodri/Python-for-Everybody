# Exercise 4: Find all unique words in the file romeo.txt and read it line by line. For each line, 
# split the line into a list of words using the split function. For each word, check to see if the word 
# is already in the list of unique words. If the word is not in the list of unique words, add it to the list.
# When the program completes, sort and print the list of unique words in alphabetical order.

lst = open('romeo.txt').read().split() # Reading the file and split to create a list of words
uniques = []
for word in lst: # For each word in the list
    if word not in uniques: # Check to see if the word is already in the list of unique words
        uniques.append(word) #  If the word is not in the list of unique words, add it to the list
uniques.sort() # Sort and print
print(uniques)