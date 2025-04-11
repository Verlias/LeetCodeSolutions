class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        res = 0
        for i in nums:
            if not(i >= k):
                res += 1
        return res
        