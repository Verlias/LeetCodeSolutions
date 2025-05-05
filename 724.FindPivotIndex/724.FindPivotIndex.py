class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_prefix = 0
        l_nums = []
        right_prefix = 0
        r_nums = []
        for i in range(0, len(nums)):
            left_prefix += nums[i]
            l_nums.append(left_prefix)
        
        for j in range(len(nums) - 1, -1,-1):
     
            right_prefix += nums[j]
            r_nums.insert(0, right_prefix)

        
        for i in range(0, len(nums)):
            if r_nums[i] == l_nums[i]:
                return i

        return -1