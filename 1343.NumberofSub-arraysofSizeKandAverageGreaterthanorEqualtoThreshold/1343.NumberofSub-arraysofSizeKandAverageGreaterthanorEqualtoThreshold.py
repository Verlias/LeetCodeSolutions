class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        L = 0
        total = 0
        res = 0
        for R in range(len(arr)):
            total += arr[R]
            if (R-L) + 1 > k:
                total -= arr[L]
                L += 1
            if (total / k) >= threshold and (R-L) + 1 == k:
                res += 1
          
        return res

             

