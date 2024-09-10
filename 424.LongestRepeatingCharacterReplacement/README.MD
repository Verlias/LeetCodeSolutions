# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
Sliding window to find the longest substring

# Approach
<!-- Describe your approach to solving the problem. -->
* Two Sentence Summary: Extend sliding window till the number of characters is greater than k, and once that occurs contract the window. Use hashmaps to keep track of the count of characters in the array so you know when its greater than k.
* loop through the string and increment the count of each character and keep track of the highest frequency character at each step.
* once the window gets to a point where there are too many characters to replace (greater than k), then move the window over to check for a greater window.
* Return the length of the window. the reason why you dont have to keep track is because the max window is valid at each step.

# Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->
O(N)

- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
O(N)

# Code
```
class Solution(object):
    def characterReplacement(self, s, k):
        count = {}
        l = 0
        maxf = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])

            if (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1

        return (r - l + 1)


        
```