class Solution(object):
    def reverseString(self, s):
        #Modify in Place with Two pointer method

        l, r = 0, len(s) - 1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
        return s