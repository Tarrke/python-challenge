from PIL import Image
import urllib.request
import os
from io import BytesIO
import base64

username = 'huge'
password = 'file'

req = urllib.request.Request("http://www.pythonchallenge.com/pc/return/cave.jpg")

credentials = ('%s:%s' % (username, password))
encoded_credentials = base64.b64encode(credentials.encode('ascii'))
req.add_header('Authorization', 'Basic %s' % encoded_credentials.decode("ascii"))
response = urllib.request.urlopen(req)

img = Image.open(BytesIO(response.read()))

(w, h) = img.size

even = Image.new('RGB', (w // 2, h // 2))
odd = Image.new('RGB', (w // 2, h // 2))

for i in range(w):
    for j in range(h):
        p = img.getpixel((i,j))
        if (i+j)%2 == 1:
            odd.putpixel((i // 2, j // 2), p)
        else:
            even.putpixel((i // 2, j // 2), p)
even.save('temp/even.jpg')
odd.save('temp/odd.jpg')