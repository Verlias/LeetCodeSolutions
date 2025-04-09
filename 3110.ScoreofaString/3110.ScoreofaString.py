class Solution:
    def scoreOfString(self, s: str) -> int:
        sum = 0
        for char in range(0,len(s) - 1):
            diff =  abs(ord(s[char]) - ord(s[char + 1]))
            sum += diff
        return sum
        