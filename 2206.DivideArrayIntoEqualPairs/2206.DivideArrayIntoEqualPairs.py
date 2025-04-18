class Solution:
    def divideArray(self, nums: List[int]) -> bool:

        hashmap = {}
        res = 0 
        for i in nums:
            hashmap[i] = 1 + hashmap.get(i,0)
        
        for key,value in hashmap.items():
            if value % 2 == 0:
                res += value // 2
            else:
                return False
        
        if (2 * res == len(nums)):
            return True
        