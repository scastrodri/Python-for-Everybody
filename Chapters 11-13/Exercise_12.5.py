#  Exercise 5: (Advanced) Change the socket program so that it only shows data after the headers and a blank 
# line have been received. Remember that recv receives characters (newlines and all), not lines.

from email import header
import socket
url = input('Please enter a url: ') # Prompt the user for the URL
try:
    host = url.split('/')[2] # Using split('/') to break the URL into its component to extract the host name
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((host, 80)) # Socket connect to port 80
    cmd = ('GET ' + url + ' HTTP/1.0\r\n\r\n').encode()
    mysock.send(cmd)
except:
    print('The url: ' + url + ' is not valid')
    quit()

while True:
        data = mysock.recv(512)
        if (len(data) < 1):
            break
        data = data.decode()
        pos = data.find("\r\n\r\n") # Find the position_ 
        print(data[pos+4:], end="") # Print from the position + 4 (to exclude "\r\n\r\n")
mysock.close()