# Exercise 2: Write a program to look for lines of the form: 'New Revision: 39772' Extract the number from each 
# of the lines using a regular expression and the findall() method. Compute the average of the numbers and print 
# out the average as an integer.

from audioop import avg
from operator import le
import re
fhand = open('mbox.txt')
count = 0
lst = list()
for line in fhand:
    line = line.strip()
    x = re.findall('New Revision: ([0-9]+)',line) # look for lines of the form: 'New Revision: 39772' Extract the number
    if len(x)>0:
        lst = lst + x
lst = list(map(int,lst)) # the map function executes a specified function for each item in an iterable. The item is sent to the function as a parameter.
average = int(sum(lst)/len(lst))
print(average)