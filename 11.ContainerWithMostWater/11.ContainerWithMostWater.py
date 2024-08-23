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