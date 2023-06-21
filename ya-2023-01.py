#!/usr/bin/python3

import copy
a = [4, 5, 2, 2, 4, 2] # -> [3, 4, 1, 1, 3, 1] -> [2, 3, 0, 0, 2, 0] 
b = a.copy()

# The first solution, brute force, could be much more ops than O(N), depens from queues length.
i, entrance = 0, 0
while a[entrance] > 0: 
    i += 1
    entrance = i % len(a)
    a[entrance] -= 1 + 1 * i % len(a)
    print("{}, {}, {}".format(a, i, entrance))
print(entrance + 1) # Human readable is needed?

# The second approach, max O(2N), the 'min' and 'index' methods have O(N) complexity.
print(b.index(min(b)) + 1)

