# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
* You need a stack to keep track of the current number you are on, such that you are able to update the result based on certain conditions.

# Approach
<!-- Describe your approach to solving the problem. -->
* Essentially to solve this problem you iterate over a cirrcular Array (array * 2) and append all values in the array such that it ends at the end of the original array. From there you would operate and update the result array based on certain conditions and return the result.

* declare variable named n = to the len of nums
* declare a stack array
* result array with the default of -1 with len of nums
* iterate through the indexs of nums array. in range of * 2 of len(nums), so it could simulate a cirrcular array
* before any appending or checking find the index. This is done by doing the current iteration divided by len(nums). The reason why is because this would allow us to get indexs within our original array
* while loop to check if anything is in the stack. if so then check if the current number on the iteration in the array is greater than the value in the stack
* if so pop that value and get the index
* then append that result to that popped index and make it equal to that greater than value
* outside of while loop append all indexes to the stack. as long as its current iteraztion is less than the length
* return value.

# Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->
O(N)

- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```
class Solution(object):
    def nextGreaterElements(self, nums):
        n = len(nums)
        result = [-1] * n
        stack = []
        for i in range(2 * n):
            index = i % n
            while stack and nums[index] > nums[stack[-1]]:
                val = stack.pop()
                result[val] = nums[index]

                
            if i < n:
                stack.append(i)

        return result

        


        
```