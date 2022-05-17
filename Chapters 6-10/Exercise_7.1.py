# Exercise 1: Write a program to read through a file (mbox-short.txt) and print the contents of the file 
# (line by line) all in upper case. 

fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()
for line in fhand:
    line = line.rstrip()
    print(line.upper())