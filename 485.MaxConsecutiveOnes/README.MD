# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
I could use a sliding window algorithm to capture all values of 1's 

# Approach
<!-- Describe your approach to solving the problem. -->
* Two Sentence Solution: Extend Window till the right pointer hits a zero & Update Maxiumum number of consectutive ones each step. Never Count for the zero in the array, if there is a zero in the array skip the left pointer to the value after the zero. - Visual Way: Expand window all the way before it sees a zero. Once it sees a zero move left pointer to the next value thats not a zero and continously expand.
* declare left and right pointers at the first index. As well as declaring a best max variable
* Iterate through each value in the array and increment the right pointer each time 1 appears. As well as update the best_max by the difference from the right and left pointer plus 1. (plus 1 because its doing from a 1 to 1, not zero to another zero/ zero to another one)
* contract left pointer once a zero appears and move it to the next value in the array thats not a zero.
* Return value.


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
    def findMaxConsecutiveOnes(self, nums):
        l = 0
        r = 0
        best_max = 0
        for num in nums:
            #Expand Window - Till we see a 0
            if num == 1:
                #Process Window
                best_max = max(best_max, r - l + 1)
                r += 1
            else:
                #Contract Window - Till we see a 0
                r += 1
                l = r
        return best_max
        
```