# Exercise 2: Change your socket program so that it counts the number of characters it has received and stops 
# displaying any text after it has shown 3000 characters. The program should retrieve the entire document and 
# count the total number of characters and display the count of the number of characters at the end of the document.

import socket
url = input('Please enter a url: ') # Prompt the user for the URL
count = 0
try:
    host = url.split('/')[2] # Using split('/') to break the URL into its component to extract the host name
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((host, 80)) # Socket connect to port 80
    cmd = ('GET ' + url + ' HTTP/1.0\r\n\r\n').encode()
    mysock.send(cmd)
except:
    print('The url: ' + url + ' is not valid')
    exit()
while True:
    data = mysock.recv(512)
    for c in data: # Loop through the data
        count += 1
    if len(data) < 1 or count >= 3000: # condition to stop at 3000 characters
        break
    print(data.decode(),end='')
print(count)
mysock.close()