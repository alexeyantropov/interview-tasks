#!/usr/bin/python3

import copy
#    e=1                        e=2                   e=3
a = [1, 5, 2, 2, 4, 2] # -> [0, 4, 1, 1, 3, 1] -> [0, 3, 0, 0, 2, 0] 
b = a.copy()

i, entrance = 0, 0
while a[entrance] > 0: 
    i += 1
    entrance = i % len(a)
    a[entrance] -= 1 + 1 * i % len(a)
    # print("{}, {}, {}".format(a, i, entrance))
print(entrance + 1) # Human readable is needed?
