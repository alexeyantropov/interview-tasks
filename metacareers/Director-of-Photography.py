# Write any import statements here
cases = [[5, 'APABA', 1, 2], [5, 'APABA', 2, 3], [8, '.PBAAP.B', 1, 3]]
# APABA
# _PAB_
#
# .PBAAP.B
# _P__A__B
# __B_AP__
# __BA_P__

def getArtisticPhotographCount(N: int, C: str, X: int, Y: int) -> int:
    # Write your code here
    ret = set()
    for i in range(N):
        pP, pA, pB = None, None, None
        if C[i] != 'P':
            continue
        pP = i
        j = i - 1
        while j >= 0 and X <= i - j <= Y:
            if C[j] != 'A':
                j -= 1
                continue
            pA = j
            k = j - 1
            while k >= 0 and X <= j - k <= Y:
                if C[k] != 'B':
                    k -= 1
                    continue
                pB = k
                photoset = '{}{}{}'.format(pP, pA, pB)
                ret.add(photoset)
                print(photoset)
                k -= 1
            j -= 1
        # and to the right
        j = i + 1
        while j < N and X <= j - i <= Y:
            if C[j] != 'A':
                j += 1
                continue
            pA = j
            k = j + 1
            while k < N and X <= k - j <= Y:
                if C[k] != 'B':
                    k += 1
                    continue
                pB = k
                photoset = '{}{}{}'.format(pP, pA, pB)
                ret.add(photoset)
                print(photoset)
                k +=1
            j += 1

    return(len(ret))

for case in cases:
  print(getArtisticPhotographCount(*case))