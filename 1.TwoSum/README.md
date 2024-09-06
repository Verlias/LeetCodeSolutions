# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
I could solve this with two pointers if sorted. I could also solve this by keeping track of values that I've pasted in a dictionary.

# Approach
<!-- Describe your approach to solving the problem. -->
* Two Sentence Summary: Keep track of the values and indexes you pasted while iterating through the array. Check if the difference between the target number and current value is in the dict and if so return the pair of indexes  
* HashMap Solution:
* loop through nums with enumerate and save every value and the index of that value
* Each time in the loop check if the difference between the target and the current value is in the dict
* If so return the pair if indexes
* Two Pointer Solution: 
* sort array and increment pointers based on the sum total value.
* If too small increment left pointer vice versa.

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
    def twoSum(self, nums, target):
        dict = {}
        for i, val in enumerate(nums):
            diff = target - val
            if diff in dict:
                return [dict[diff], i]
            dict[val] = i


        
```