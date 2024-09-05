class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False

        c1 = {}
        c2 = {}

        for i in range(len(s)):
            c1[s[i]] = 1 + c1.get(s[i],0)
            c2[t[i]] = 1 + c2.get(t[i],0)
        
        return c1 == c2
