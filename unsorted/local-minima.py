#!/Users/aleksey.antropov/miniconda/bin/python3
"""
Find local minimas for given function and return them as a list,
return an empy list if there aren't any local minimas. 
Note about: https://en.wikipedia.org/wiki/Maximum_and_minimum .
"""
graphs = [
    [3,1,2,0,6],            # 0, 1
    [6,-3,0,2,0,-1,0],      # -3, -1, from Wiki
    [4,2,2,1,3],            # 1
    [1],                    # None
    [2,1],                  # None
    [3,2,1],                # None
    [2,1,3],                # 1
]

def local_minima(arr: list) -> list:
    # The corner cases.
    if len(arr) == 3 and arr[0] > arr[1] < arr[2]:
        return([arr[1]])
    elif len(arr) == 3 or len(arr) < 3:
        return([])
    else:
        pass
    # The general idea is there.
    ret = set()
    for i in range(1, len(arr) - 1):
        if arr[i-1] > arr[i] < arr[i+1]:
            ret.add(arr[i])
    return(list(ret))

for g in graphs:
    print('in: {}, out: {}'.format(g, local_minima(g)))
