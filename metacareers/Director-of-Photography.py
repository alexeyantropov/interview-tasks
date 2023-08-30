# Write any import statements here
cases = [[5, 'APABA', 1, 2], [5, 'APABA', 2, 3], [8, '.PBAAP.B', 1, 3]]
# APABA
# _PAB_
#
# .PBAAP.B
# _P__A__B
# __B_AP__
# __BA_P__

""""
# The first solution. There is a lot of copy-paste here on lines when
# sub loops traverse from an protographer to an actor and a backdrop.
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
                k +=1
            j += 1

    return(len(ret))
"""

def getArtisticPhotographCount(N: int, C: str, X: int, Y: int) -> int:
    ret = set()

    for i in range(N):
        # The 'i' var is a pointer to an actor.
        if C[i] != 'A':
            continue
        # The jL and jR vars are pointers to a photographer.
        jL, jR = i - 1, i + 1
        while jL >= 0 and jR < N and (X <= abs(i-jL) <= Y or X <= abs(i-jR <= Y)):

            if C[jL] == 'P' and X <= abs(i-jL) <= Y:
                k = i + 1
                while k < N and X <= abs(i-k) <= Y:
                    if C[k] == 'B':
                        ret.add('{}.{}.{}'.format(jL, i, k))
                    k += 1

            if C[jR] == 'P' and X <= abs(i-jR) <= Y:
                k = i - 1
                while k >= 0 and X <= abs(i-k) <= Y:
                    if C[k] == 'B':
                        ret.add('{}.{}.{}'.format(k, i, jR))
                    k -= 1

            jL, jR = jL - 1, jR + 1

    return(len(ret))

for case in cases:
    print(getArtisticPhotographCount(*case))