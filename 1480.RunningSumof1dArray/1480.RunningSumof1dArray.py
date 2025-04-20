class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        prefix_sum = 0
        res = []
        for val in nums:
            prefix_sum += val
            res.append(prefix_sum)
        return res
        