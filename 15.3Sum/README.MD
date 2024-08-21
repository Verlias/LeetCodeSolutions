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
    def threeSum(self, nums):
        nums.sort()
        result = []

        for i, j in enumerate(nums):
            if i > 0 and j == nums[i-1]:
                continue
        
            first_pointer = i + 1
            second_pointer = len(nums) - 1

            while first_pointer < second_pointer:
                sum = j + nums[first_pointer] + nums[second_pointer]

                if sum > 0:
                    second_pointer -= 1
                elif sum < 0:
                    first_pointer += 1
                else:
                    result.append([j,nums[first_pointer],nums[second_pointer]])
                    first_pointer += 1
                    while nums[first_pointer] == nums[first_pointer - 1] and first_pointer < second_pointer:
                        first_pointer += 1

        return result




        
```