#/usr/bin/python

# this script creates an index file with html to list files in /var/pub (by default)
# accompanying js is in the images.html page
# change value of dir in like 8 if you feel like it

import os
dir = os.listdir('/var/pub')

index = open('index', 'w')

for file in dir:
    index.write(f'<a href="/var/pub/{file}">{file}</a><br>')

index.close()