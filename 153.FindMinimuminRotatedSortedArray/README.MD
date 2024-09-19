# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
Binary search to find which section of the array the minimum value is located at.z
# Approach
<!-- Describe your approach to solving the problem. -->
* Two Sentence Summary: Binary search to figure out which portion of the array should be searched. Once portion of array is found where the minimum value could be, binary search could be continued to executed in there.
* Implement Binary Search
* Compare mid point to right pointer and move left pointer to the index right of previous mid (if mid is greater than  the right most pointer. this means the minimum value is on the right side of the array)
* if it doesnt satisify the previous condition then the minimum value is on the left portion of the array so move the right pointer to the previous mid point value, to include the prev mid to be checked.

# Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->
O(Log(N))

- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
O(1)

# Code
```
class Solution(object):
    def findMin(self, nums):
        l = 0
        r = len(nums) - 1
        while l < r:
            mid = (r + l) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        return nums[l]




        
```