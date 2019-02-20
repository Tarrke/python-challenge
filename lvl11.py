from PIL import Image
from urllib.request import urlopen
from urllib.parse import urlencode, quote_plus
import os
from io import BytesIO

username = 'huge'
password = 'file'
values = { 'username': username,'password': password }
data = urlencode(values, quote_via=quote_plus)

response = urlopen("http://www.pythonchallenge.com/pc/return/cave.jpg", data=data)
img = Image.open(BytesIO(response.content))

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
even.save('even.jpg')
odd.save('odd.jpg')