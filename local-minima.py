#!/Users/aleksey.antropov/miniconda/bin/python3

# Task: Find a local minima on function values
# The test set:
test_sets = [
    [3,1,4,5,11,2,15,6],    # 1, 4, 2, 6
    [7,7,4,5,11,13,15,6],   # 4, 5, 11, 6
    [1],                    # 1
    [2,1],                  # 1
    [3,2,1],                # 2, 1
    [2,1,3],                # 1
]
# A function to add only uniq elemets of list:
def add_to_arr(arr: list, val: int) -> list:
    if val in arr:
        return(arr)
    else:
        return(arr + [val])
# The first implementaion.
def local_minima_one(arr: list) -> list:
    ret = []
    if len(arr) < 2:
        return(arr)
    if len(arr) < 3:
        return([min(arr)])
    for i in range(len(arr)):
        # Borders.
        if (i == 0 or i == len(arr)-2) and arr[i] != arr[i+1]:
            if arr[i] < arr[i+1]:
                ret =  add_to_arr(ret, arr[i])
            else:
                ret = add_to_arr(ret, arr[i+1])
        # The main part.
        if i > 1 and i < len(arr)-2:
            if arr[i-1] < arr[i] and arr[i-1] < arr[i+1]:
                ret = add_to_arr(ret, arr[i-1])
            if arr[i] < arr[i-1] and arr[i] < arr[i+1]:
                ret = add_to_arr(ret, arr[i])
            if arr[i+1] < arr[i-1] and arr[i+1] < arr[i]:
                ret = add_to_arr(ret,arr[i+1])
    return(ret)
# The second implementaion, with the build-int min() finction.
def local_minima_two(arr: list) -> list:
    ret = []
    if len(arr) < 2:
        return(arr)
    if len(arr) < 3:
        return([min(arr)])
    for i in range(len(arr)):
        # Borders.
        if (i == 0 or i == len(arr)-2) and arr[i] != arr[i+1]:
            ret =  add_to_arr(ret, min(arr[i], arr[i+1]))
        if i > 1 and i < len(arr)-2:
            tmp = min(arr[i-1], arr[i], arr[i+1])
            if arr.count(tmp) == 1:
                ret = add_to_arr(ret, tmp)
    return(ret)

for test_set in test_sets:
    print(local_minima_one(test_set))
    print(local_minima_two(test_set))