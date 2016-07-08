# -*- coding: utf-8 -*-
__author__ = 'boonya'
# http://www.pythonchallenge.com/pc/def/map.html

import string
from collections import deque

bad_alphabet = deque(string.ascii_lowercase)
bad_alphabet.rotate(2)

replacer = string.maketrans(''.join(bad_alphabet), string.ascii_lowercase)

# text = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw " \
#        "fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq " \
#        "pcamkkclbcb. lmu ynnjw ml rfc spj."

text = "map.html"

true_text = text.translate(replacer)

print true_text
