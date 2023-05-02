#!/Users/aleksey.antropov/miniconda/bin/python3
"""
Find local minimas for given function and return them as list.
Return 'None' if there isn't any local minimas.
Note about: https://en.wikipedia.org/wiki/Maximum_and_minimum .
"""
graphs = [
    [3,1,2,0,6],            # 0, 1
    [4,2,2,1,3],            # 1
    [1],                    # None
    [2,1],                  # None
    [3,2,1],                # None
    [2,1,3],                # 1
]

def local_minima(arr: list) -> list:
    # Corner cases.
    if len(arr) < 3:
        return(None)
    elif len(arr) == 3 and arr[0] > arr[1] < arr[2]:
        return([arr[1]])
    elif len(arr) == 3:
        return(None)
    else:
        pass
    # Main logic.
    ret = set()
    for i in range(1, len(arr) - 1):
        if arr[i-1] > arr[i] < arr[i+1]:
            ret.add(arr[i])
    return(list(ret))

for g in graphs:
    print('in: {}, out: {}'.format(g, local_minima(g)))
