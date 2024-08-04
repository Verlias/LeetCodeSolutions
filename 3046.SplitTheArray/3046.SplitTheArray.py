class Solution(object):
    def isPossibleToSplit(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        count_number = Counter(nums)

        for i in count_number.values():
            if i > 2:
                return False

        return True
            
                