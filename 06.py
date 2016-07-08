import zipfile
import re

nothing = 90052
pairs = []

zip = zipfile.ZipFile("/Users/boonya/Downloads/channel.zip", "r")

while True:
    file = str(nothing) + '.txt'
    content = zip.read(file)
    try:
        match = re.search('nothing is (\d+)', content)
        pairs.append(zip.getinfo(file).comment)
        nothing = match.group(1)
        nothing = int(nothing)
    except AttributeError:
        break

print ''.join(pairs)