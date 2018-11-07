"""
Created on Wed Nov  7 18:02:35 2018

@author: sajid Ullah
"""

import urllib.request

try:
    urllib.request.urlopen("http://google.com", timeout=2)
    print ("working connection")

except urllib.request.URLError:
    print ("No internet connection")
