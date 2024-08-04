# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->

# Approach
<!-- Describe your approach to solving the problem. -->

# Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```
class Solution(object):
   def twoSum(self, nums, target):
        hashset = set(nums)
        for i in range(0,len(nums)):
            # Values - each index and finds if there is a true value 
            x = target - nums[i]
            # if there is a (value - x) within the set and its not the same number previously used to subtract return the indices
            if (x) in hashset and nums.index(x) != i:
                return [i, nums.index(x)]
        return []



        
```