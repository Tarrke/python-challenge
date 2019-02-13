import urllib.request
import re

base_url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
code = '12345' # First clue
code = '8022'  # Second clue
r = re.compile(r'and the next nothing is ([0-9]+)')

while True:
    url = base_url + code
    print("~~ Get:", url)
    resp = urllib.request.urlopen(url)
    html = resp.read()
    print(html)
    code = re.findall(r, str(html))[0]
    print(code)

# => ~~ Get: http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=16044
# => b'Yes. Divide by two and keep going.'
# => ~~ Get: http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=66831
# => b'peak.html'