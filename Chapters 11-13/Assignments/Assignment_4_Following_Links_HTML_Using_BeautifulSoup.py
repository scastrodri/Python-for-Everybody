# In this assignment you will write a Python program that expands on http://www.py4e.com/code3/urllinks.py. 
# The program will use urllib to read the HTML from the data files below, extract the href= vaues from the anchor 
# tags, scan for a tag that is in a particular position relative to the first name in the list, follow that link 
# and repeat the process a number of times and report the last name you find.

from turtle import position
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Please enter the URL: ')
count = int(input('Please enter the number of counts: '))
position = int(input('Please enter the initial potition: '))

while count > 0:
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    url = tags[position - 1].get('href', None)
    count = count - 1
print (url)