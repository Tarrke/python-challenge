import os
import zipfile
import io
import requests
import re

# Creating temp dir
if not os.path.exists('lvl6temp'):
    os.mkdir('lvl6temp')
os.chdir('lvl6temp')

# Get the zip file
zip_file_url = 'http://www.pythonchallenge.com/pc/def/channel.zip'
r = requests.get(zip_file_url)
z = zipfile.ZipFile(io.BytesIO(r.content))
z.extractall()

rg = re.compile(r'Next nothing is ([0-9]+)')

# First file
file = '90052'
a = z.getinfo(file+'.txt').comment.decode('utf-8')
while True:
    try:
        with open(file+'.txt') as fichier:
            s = fichier.read()
            file = re.findall(rg, s)[0]
            #print('Next:', file)
            print(z.getinfo(file+'.txt').comment)
            a = a + str(z.getinfo(file+'.txt').comment.decode('utf-8'))
    except Exception as e:
        print(e)
        break


print(a)

# Remove temp dir
