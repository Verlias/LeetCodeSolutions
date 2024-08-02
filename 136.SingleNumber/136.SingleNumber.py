class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hashtable = defaultdict(int)
        for i in nums:
            hashtable[i] += 1
        
        for key, value in hashtable.items():
            if value == 1:
                return key
