class Solution(object):
    def lengthOfLongestSubstring(self, s):
        hashset = set()
        l = 0
        res = 0
        for i in range(len(s)):
            while s[i] in hashset:
                hashset.remove(s[l])
                l += 1
            hashset.add(s[i])
            res = max(res, i - l + 1)
        
        return res