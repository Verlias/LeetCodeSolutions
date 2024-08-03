class Solution(object):
    def canBeEqual(self, target, arr):
        """
        :type target: List[int]
        :type arr: List[int]
        :rtype: bool
        """
        if sorted(reversed(arr)) == sorted(target):
            return True
        else:
            return False
        