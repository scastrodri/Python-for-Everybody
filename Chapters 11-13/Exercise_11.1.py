# Exercise 1: Write a simple program to simulate the operation of the grep command on Unix. Ask the user to enter 
# a regular expression and count the number of lines that matched the regular expression:
'''
^Author
^X-
java$
'''

import re
reg_exp = str(input('Enter a regular expression: '))
fhand = open('mbox.txt')
count = 0
for line in fhand:
    line = line.strip()
    if re.findall(reg_exp,line) != []:
        count += 1
print(count)