class Solution(object):
    def majorityElement(self, nums):
        hashmap = {}
        #Frequency
        for i in nums:
            hashmap[i] = 1 + hashmap.get(i,0)

        for i, j in hashmap.items():
            if j == max(hashmap.values()):
                return i