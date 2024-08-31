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

        