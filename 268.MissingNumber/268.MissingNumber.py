class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        hashset = set()
        for i in range(0,len(nums) + 1):
            hashset.add(i)
        for i in nums:
            if i in hashset:
                hashset.remove(i)
        res = hashset.pop()
        return res
        
        