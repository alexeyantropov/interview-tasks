a = [1, 2, 3]

def f(x):
    x += [0]
    return(x)

b = f(a)

print(a, b)
