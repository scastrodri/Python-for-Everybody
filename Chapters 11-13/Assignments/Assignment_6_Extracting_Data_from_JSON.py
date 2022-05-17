# In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/json2.py. The 
# program will prompt for a URL, read the JSON data from that URL using urllib and then parse and extract the 
# comment counts from the JSON data, compute the sum of the numbers in the file and enter the sum below:

import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    url = input('Please enter the URL ')
    if len(url) < 1: break
    
    data = urllib.request.urlopen(url, context=ctx).read()
      
    try:
        js = json.loads(data)
    except:
        js = None
    
    nums = list()
    for item in js['comments']:
        nums.append(int(item["count"]))
    print(sum(nums))