class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        res = 0
        hashmap = {}

        for i in nums:
            hashmap[i] = 1 + hashmap.get(i,0)
        for key, value in hashmap.items():
            if value == 1:
                res += key
        return res
        