class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        l = 0
        r = 0
        best_max = 0
        while r < len(nums):
            if nums[r] == 1:
                best_max = max(best_max, r - l + 1)
                r += 1
            else:
                r += 1
                l = r
        return best_max
