# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
I could use a sliding window algorithm to capture all values of 1's. While Continously Moving.

# Approach
<!-- Describe your approach to solving the problem. -->
* Two Sentence Solution: Span the window sliding window till it reaches the count of zeros greater than k then find the distance between the right and left pointers. If theres an edge case where the count of zeros is less than or equal to k when the array ends then do the right pointer minus left.
* Declare variables for the left, right pointers as well as best_max and count of zero variables.
* iterate through the array with a while loop incrementing the right pointer each step at the END.
* increment the count of zeros by 1 each time the right pointer sees a zero.
* If the count of zero is greater than the value of k, then find the best_max by doing the right pointer index minus left. Then decrement the count of zeros by one each time the left pointer sees a zero (left pointer continous increments each step in the nested while loop)
* Edge Case: If the count of zero never exceeds the value of k that means the it mustve reached to the end of the array, so find the best_max.


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
    def longestOnes(self, nums, k):
        l = 0
        r = 0
        best_max = 0 
        count_of_zeros = 0

        #Iterate through Array
        while r < len(nums):
            #Keeps Track of the Count of zeros pasted
            if nums[r] == 0:
                count_of_zeros += 1
            
            while count_of_zeros > k:
                #Process Window
                best_max = max(best_max, r - l )
                #Contract Window
                if nums[l] == 0:
                    count_of_zeros -= 1
                l += 1
            #Expands Window
            r += 1
        #Edge Case
        if count_of_zeros <= k:
            best_max = max(best_max, r - l)

        return best_max
            
```