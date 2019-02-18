from urllib.request import urlopen
import png, re

response = urlopen("http://www.pythonchallenge.com/pc/def/oxygen.png")

(w, h, rgba, dummy) = png.Reader(response).read()

it = list(rgba)
mid = int(h / 2)
l = len(it[mid])
res = [chr(it[mid][i]) for i in range(0, l, 4*7) if it[mid][i] == it[mid][i + 1] == it[mid][i + 2]]
# Print message
print("".join(res))

# Extract list of integers
l = list(map(int, list(re.findall(r'\d+', "".join(res)))))
# Convert into characters
s = "".join(list(map(chr, l)))
print(s)