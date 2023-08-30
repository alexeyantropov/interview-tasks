#!/Users/aleksey.antropov/miniconda/bin/python3
# Task: Reverse a list with all possible methods you know.
a = [1,2,3,4,5]

def method_slice(l):
    return(l[::-1])

def method_generator(l):
    return([x for x in reversed(a)])

def method_inplace_reverse(l):
    t = l.copy() # Just a sample!
    t.reverse()
    return(t)

def method_inplace_two_pointers(arr):
    t = arr.copy()
    l, r = 0, len(t) - 1
    while l < r:
        t[l], t[r] = t[r], t[l]
        l += 1
        r -= 1
    return(t)

print(method_slice(a))
print(method_generator(a))
print(method_inplace_reverse(a))
print(method_inplace_two_pointers(a))
