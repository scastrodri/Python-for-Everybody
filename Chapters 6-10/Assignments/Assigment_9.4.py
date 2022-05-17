# Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail 
# messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent 
# the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number 
# of times they appear in the file. After the dictionary is produced, the program reads through the dictionary 
# using a maximum loop to find the most prolific committer.

fhandle = open(input("Enter file:"))
words = list()
count = dict()
bigcount = None
bigword = None
for line in fhandle:
    if line.startswith("From "):
        words.append((line.split()[1]))
for word in words:
    count[word] = count.get(word,0)+1
for key,value in count.items():
    if bigcount is None or value > bigcount:
        bigcount = value
        bigword = key
print(bigword, bigcount)