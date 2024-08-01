class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hashset = set(nums)
        longest_streak = 0
        
        for num in hashset:
            # Check if it's the start of a sequence
            if num - 1 not in hashset:
                current_num = num
                current_streak = 1
                
                while current_num + 1 in hashset:
                    current_num += 1
                    current_streak += 1
                
                longest_streak = max(longest_streak, current_streak)
        
        return longest_streak
