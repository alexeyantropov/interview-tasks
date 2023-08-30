a = [2,7,5,11,15]
target = 12
memo = dict()
ret = []

for i in range(len(a)):
    desire = target - a[i]
    print(a[i], desire, memo)
    if desire in memo:
        ret = [memo[desire], i]
        break
    else:
        memo[a[i]] = i
print(ret)