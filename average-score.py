# HackerRank: Sort hotels by average score. Each line of input had the hotel ID and a review score.
data = [
[1000, 4],
[1000, 7],
[2000, 10],
[2000, 8],
]

score_counts = {} # A tmp dict with count of the scrores
score_sums = {} # A tmp dict with total amount of the score
ret = {} # Another tmp dict for results

for i in range(len(data)): # O(N)
    hotel = data[i][0]
    score = data[i][1]
    if hotel in ret: # O(1)
        score_counts[hotel] += 1
        score_sums[hotel] += 1
    else:
        ret[hotel] = 0
        score_counts[hotel] = 1
        score_sums[hotel] = score
        
for hotel in ret.keys(): # O(N)
    ret[hotel] = score_sums[hotel] / score_counts[hotel]

ret_ = (sorted(ret.items(), key=lambda x: x[1], reverse=True)) # the sort() func is overate O(N*Log(N))
print(ret_) # [(2000, 5.5), (1000, 2.5)]