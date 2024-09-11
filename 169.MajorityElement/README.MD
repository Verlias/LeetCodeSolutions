# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
Hashmap to count the frequencies
# Approach
<!-- Describe your approach to solving the problem. -->
* Two Sentence Summary: Count the frequencies using a hashmap and returning the hashmap key when its max.
* create hashmap
* count frequencies using loop storing it in a hashmap
* returning the hashmap key when its max.

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
    def majorityElement(self, nums):
        hashmap = {}
        #Frequency
        for i in nums:
            hashmap[i] = 1 + hashmap.get(i,0)

        for i, j in hashmap.items():
            if j == max(hashmap.values()):
                return i


        
```