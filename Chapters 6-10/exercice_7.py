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