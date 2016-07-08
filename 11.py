# -*- coding: utf-8 -*-
__author__ = 'boonya'
# http://www.pythonchallenge.com/pc/return/5808.html

import requests
from PIL import Image
from StringIO import StringIO
import math

r = requests.get('http://www.pythonchallenge.com/pc/return/cave.jpg',
                 auth=('huge', 'file'))
im = Image.open(StringIO(r.content))

o_pixels = list(im.getdata())
n_im = Image.new('RGB', (im.size[0], im.size[1]), 0)
n_im.putdata(o_pixels[::2])
n_im.save("cave.jpg")
