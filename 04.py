# 12345
# and the next nothing is 44827
# http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345
import requests
import re

nothing = 12345
linkedlist = []

while True:
    r = requests.get('http://www.pythonchallenge.com/pc/def/linkedlist.php',
                     params={'nothing': nothing})

    linkedlist.append(nothing)
    print "Text: ", r.text
    print "Nothing: ", nothing

    if 200 != r.status_code:
        print "status_code is not equal 200."
        break

    try:
        match = re.search('nothing is (\d+)', r.text)
        nothing = match.group(1)
        nothing = int(nothing)
    except AttributeError:
        if "Divide by two" in r.text:
            nothing /= 2
        else:
            print "re.search AttributeError."
            break

    if not nothing:
        print "not nothing."
        break

print "linkedlist: ", linkedlist