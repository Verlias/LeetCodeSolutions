# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->


# Approach
<!-- Describe your approach to solving the problem. -->
One-Two Sentence summary on how to solve the problem:
Using Two Pointers to find the biggest height in the Array. All while computing the Area for each pointer... saving the MaxArea and returning it.

# Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->
O(N)

- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```
class Solution(object):
    def maxArea(self, height):
        l = 0 
        r = len(height) - 1
        maxArea = 0

        while l < r:
            currentArea = (r - l) * min(height[l], height[r])
            maxArea = max(maxArea, currentArea)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return maxArea


        
```