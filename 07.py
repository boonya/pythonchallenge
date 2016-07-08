import requests
from PIL import Image
from StringIO import StringIO

r = requests.get('http://www.pythonchallenge.com/pc/def/oxygen.png')

i = Image.open(StringIO(r.content))

left = 0
upper = i.size[1] / 2 - 4
right = i.size[0] - 21
lower = i.size[1] / 2 + 5

box = (left, upper, right, lower)

region = i.crop(box)

values = []
letters = []

for p in range(0, region.size[0], 7):
    point = region.getpixel((p, 1))
    letters.append(chr(point[0]))

# smart guy, you made it. the next level is [105, 110, 116, 101, 103, 114, 105, 116, 121]
print ''.join(letters)

level = []
for l in [105, 110, 116, 101, 103, 114, 105, 116, 121]:
    level.append(chr(l))

print '[105, 110, 116, 101, 103, 114, 105, 116, 121] is ', ''.join(level)
