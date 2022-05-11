# Opening files

fhand = open('mbox-short.txt') # open will be used as handler
inp = fhand.read() # reading all the file and assigning as str variable
print(len(inp)) # how many characters are
print(inp[:20]) # showing the first 20 characters

fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if line.find('@uct.ac.za') == -1: continue # Remeber the find method will return -1 if doesn't find the argument
    print(line)

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

# Exercise 2: Write a program to prompt for a file name, and then read through the file and look for lines 
# of the form: X-DSPAM-Confidence: 0.8475 When you encounter a line that starts with “X-DSPAM-Confidence:”
# pull apart the line to extract the floating-point number on the line. Count these lines and then compute 
# the total of the spam confidence values from these lines. When you reach the end of the file, print out 
# the average spam confidence.

fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()
count = 0
total = 0
for line in fhand:
    line = line.rstrip()
    if line.find('X-DSPAM-Confidence:') == -1: continue
    total = total + float(line[line.find(':') + 1:])
    count = count + 1
print('Average spam confidence: ', total/count)

# Exercise 3: Sometimes when programmers get bored or want to have a bit of fun, they add a harmless Easter Egg 
# to their program. Modify the program that prompts the user for the file name so that it prints a funny message 
# when the user types in the exact file name “na na boo boo”. The program should behave normally for all other 
# files which exist and don’t exist.

fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    if fname == 'na na boo boo':
        print ("NA NA BOO BOO TO YOU - You have been punk'd!")
        exit()
    print('File cannot be opened:', fname)
    exit()
count = 0
total = 0
for line in fhand:
    line = line.rstrip()
    if line.find('X-DSPAM-Confidence:') == -1: continue
    total = total + float(line[line.find(':') + 1:])
    count = count + 1
print('Average spam confidence: ', total/count)