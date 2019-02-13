import urllib.request
import pickle

url = 'http://www.pythonchallenge.com/pc/def/banner.p'

resp = urllib.request.urlopen(url)

obj = pickle.load(resp)

for i in range(len(obj)):
    for j in range(len(obj[i])):
        print(obj[i][j][0]*obj[i][j][1], end='')
    print('')