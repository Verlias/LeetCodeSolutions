# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
* find the correct array then execute binary search within.

# Approach
<!-- Describe your approach to solving the problem. -->
*Use binary search to find the correct array to execute binary search in

# Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->


- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->


# Code
```
class Solution(object):
    def searchMatrix(self, matrix, target):

        #Find array to execute binary search in
        lm = 0
        rm = len(matrix) - 1

        while lm <= rm:
            mid = lm + (rm - lm) / 2
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                break
            elif matrix[mid][0] < target:
                lm = mid + 1
            elif matrix[mid][-1] > target:
                rm = mid - 1    
        l = 0
        r = len(matrix[mid]) - 1

        while l <= r:
            mid_second = l + (r - l) / 2

            if matrix[mid][mid_second] == target:
                return True
            elif matrix[mid][mid_second] < target:
                l = mid_second + 1
            elif matrix[mid][mid_second] > target:
                r = mid_second - 1
        return False




        
```