# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
If the current iteration letter is the same as the first letter in needle we could compare

# Approach
<!-- Describe your approach to solving the problem. -->
* Two Sentence Summary: Iterate through the string and string slice and compare to needle, when the current iteration value is equal to the first character in needle 


# Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->
O(N)

- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
O(1)

# Code
```
class Solution(object):
    def strStr(self, haystack, needle):
        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                if haystack[i:i+len(needle)] == needle:
                    return i
        return -1


        
```