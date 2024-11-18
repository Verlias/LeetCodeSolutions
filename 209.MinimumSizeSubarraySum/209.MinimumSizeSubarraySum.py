class Solution(object):
    def minSubArrayLen(self, target, nums):
        l = 0
        total = 0
        min_length = len(nums) + 1 # the length of array plus one there cannot be a array bigger than this

        for r in range(len(nums)):
            total += nums[r]

            while total >= target:
                min_length = min(min_length, r - l + 1)
                total -= nums[l]
                l += 1
        return min_length if min_length <= len(nums) else 0
        