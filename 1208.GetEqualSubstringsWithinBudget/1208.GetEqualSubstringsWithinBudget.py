class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        max_length = 0
        total = 0
        l = 0
        for r in range(0, len(s)):
            total += abs(ord(s[r]) - ord(t[r]))
            if total > maxCost:
                total -= abs(ord(s[l]) - ord(t[l]))
                l += 1
            max_length = max(max_length, r - l + 1)
        return max_length