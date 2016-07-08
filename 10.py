# -*- coding: utf-8 -*-
__author__ = 'boonya'
# http://www.pythonchallenge.com/pc/return/bull.html

a = [1, 11, 21, 1211, 111221]

n = 5
while True:
    memory = ''
    counter = 0
    string = ''

    for index, item in enumerate(str(a[-1])):
        if index == 0:
            memory = item

        if item == memory:
            counter += 1
        else:
            string += str(counter) + memory
            counter = 1
            memory = item

    string += str(counter) + memory

    a.append(string)

    n += 1
    if n > 30:
        break

print(len(a[30]))
