#/usr/bin/python

# use this script for server side only
# creates an index file with html to list files in /var/pub (by default)
# accompanying js is in the images.html page
# change value of dir in line 8 if you feel like it
# linux ONLY unless you modify this script to work on windows

import os
import time
import sys
url = "https://cdn.furokku.pp.ua"

def fsupdate():
    dir = os.listdir('/var/pub')
    index = open('index', 'w')
    for file in dir:
        index.write(f'<li><a href="{url}/pub/{file}">{file}</a></li>')
    index.close()

while True:
    fsupdate()
    time.sleep(30)