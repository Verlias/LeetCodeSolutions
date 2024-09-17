class Solution(object):
    def findMin(self, nums):
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (r + l) // 2
            if l == r:
                return nums[l]
            elif nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        return nums[l] 


