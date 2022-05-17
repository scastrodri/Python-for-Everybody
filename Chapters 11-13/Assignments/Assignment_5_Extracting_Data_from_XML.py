# In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/geoxml.py. 
# The program will prompt for a URL, read the XML data from that URL using urllib and then parse and extract the 
# comment counts from the XML data, compute the sum of the numbers in the file.

from unittest import result
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    url = input('Please enter the URL ')
    if len(url) < 1: break
    
    data = urllib.request.urlopen(url, context=ctx).read()
    uh = urllib.request.urlopen(url, context=ctx)

    data = uh.read()
    tree = ET.fromstring(data)  
    results = tree.findall('.//comment')
    
    cont = len(results) - 1
    num = list()
    while cont >= 0:
        num.append(int(results[cont].find('count').text))
        cont = cont-1 
    print(sum(num))