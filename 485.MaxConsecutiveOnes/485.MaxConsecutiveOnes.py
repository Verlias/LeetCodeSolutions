class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        l = 0
        r = 0
        best_max = 0
        for num in nums:
            #Expand Window - Till we see a 0
            if num == 1:
                #Process Window
                best_max = max(best_max, r - l + 1)
                r += 1
            else:
                #Contract Window - Till we see a 0
                r += 1
                l = r
        return best_max

    
