# In this assignment you will read through and parse a file with text and numbers. You will extract all the 
# numbers in the file and compute the sum of the numbers.
import re
name = input("Enter file:")
handle = open(name)
numlist = list()
for line in handle:
    stuff = re.findall('[0-9]+',line)
    if len(stuff) == 0:
        continue
    for index in stuff:
        numlist.append(int(index))
print(sum(numlist))