def aboveAverageSubarrays(arr):
    output = []
    l, r = 0, 0
    
    def avg_sum(a):
        if len(a) == 0:
            return(0)
        return(sum(a)/len(a))

    while l < len(arr):
        r = l
        while r < len(arr):
            desired_arr = arr[l:r+1]
            remaining_arr = arr[0:l] + arr[r+1:]            
            if  avg_sum(desired_arr) > avg_sum(remaining_arr):
                output.append([l+1,r+1])
            r += 1
        l += 1
        
    return(output)

print(aboveAverageSubarrays([3, 4, 2]))
# output = [[1, 2], [1, 3], [2, 2]]
# The above-average subarrays are [3, 4], [3, 4, 2], and [4].