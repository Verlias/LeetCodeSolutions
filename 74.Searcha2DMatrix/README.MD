# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
* Find the bounds in which the target value is in. Ascending order gave off potentially using binary search to solve this question.

# Approach
<!-- Describe your approach to solving the problem. -->
* My current solution: iterate through each array in the 2D matrix and if target is not within the array bounds then skip it.
* Quicker Solution: binary search to find correct row, then binary search in particular row to find correct answer

# Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->


- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->


# Code
```
class Solution(object):
    def searchMatrix(self, matrix, target):
        #Iterate through each item in the matrix
        for i in matrix:
            if not (i[0] <= target <= i[-1]):
                continue
            l = 0
            r = len(i) - 1
            while l <= r:
                mid = (r + l) // 2
                if i[mid] == target:
                    return True
                elif i[mid] < target:
                    l = mid + 1
                elif i[mid] > target:
                    r = mid - 1
            
        return False





        
```