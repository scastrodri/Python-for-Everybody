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