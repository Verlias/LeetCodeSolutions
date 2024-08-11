# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
* Array is mentioned that its sorted, so the usage of two pointers and binary search is possible.

# Approach
<!-- Describe your approach to solving the problem. -->
* We have sorted Array so our options that we have is the two pointer algorithm and binary search algorithm
* The key thing about this specific problem is that its sorted in a increasing order
* This is a two pointer algorithm
* Imagine we set two pointers. One starting at first index and one at the last index
* if the sum is greater than the num then decrement the second pointer.
* If the sum is less than the target then increment the first pointer.
* Theres no needed return outside of the while loop

# Complexity
- Time complexity: O(LogN)
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```
class Solution(object):
    def twoSum(self, numbers, target):
        first_pointer = 0
        second_pointer =  len(numbers) - 1

        while first_pointer <= second_pointer:
            sum = numbers[first_pointer] + numbers[second_pointer]
            if sum == target:
                return [first_pointer + 1, second_pointer + 1]
            elif sum < target:
                first_pointer += 1
            elif sum > target:
                second_pointer -= 1
        



        
```