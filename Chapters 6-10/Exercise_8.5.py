# Exercise 5: Minimalist Email Client. Write a program to read through the mail box data and when you find 
# line that starts with “From”, you will split the line into words using the split function. You will parse 
# the From line and print out the second word for each From line, then you will also count the number of From 
# (not From:) lines and print out a count at the end.

try:
    fhand = open(input('Enter a file name: '))
    lst = []
    count = 0
    for line in fhand:
        if not line.startswith("From:"): continue
        lst = line.split()
        count = count + 1
        print(lst[1])
    print('There were ', count , ' lines in the file with From as the first word')
except:
    print('Please enter a valid file')