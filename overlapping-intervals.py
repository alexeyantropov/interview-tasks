# HackerRank: Given a list of intervals, e.g. [1,4], [2,5], [6,7], merge overlapping intervals, e.g. [1,5],[6,7].

intervals = [[1,3], [2,5], [6,7]]

# the first solution w/o stack, many extra-checks :(
ret = []
tmp = [intervals[0][0], intervals[0][1]]
for i in range(len(intervals)):
    if tmp[1] >= intervals[i][1]:
        pass
    elif tmp[1] >= intervals[i][0]:
        tmp[1] = intervals[i][1]
    else:
        tmp = [intervals[i][0], intervals[i][1]]
    if len(ret) == 0:
        ret.append(tmp)
    elif ret[-1][0] != tmp[0] and ret[-1][1] != tmp[1]:
        ret.append(tmp)
print(ret)

# more clear with a stack
ret = []
ret.append(intervals[0])
for i in range(1,len(intervals)):
    if ret[-1][0] <= intervals[i][0] <= ret[-1][1]:
        ret[-1][1] = max(ret[-1][1], intervals[i][1])
    else:
        ret.append([intervals[i][0], intervals[i][1]])
print(ret)