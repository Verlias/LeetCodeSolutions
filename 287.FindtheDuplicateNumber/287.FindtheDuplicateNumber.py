class Solution(object):
    def findDuplicate(self, nums):
        hashmap = {}
        for i in nums:
            hashmap[i] = 1 + hashmap.get(i,0)
            if hashmap[i] >= 2:
                return i

