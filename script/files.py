#/usr/bin/python

# use this script for server side only
# creates an index file with html to list files in /pub (by default)
# accompanying js is in the images.html page
# change value of dir in line 8 if you feel like it

import os
dir = os.listdir('/var/pub')
url = "https://cdn.furokku.pp.ua"

index = open('index', 'w')

for file in dir:
    index.write(f'<li><a href="{url}/pub/{file}">{file}</a></li>')

index.close()