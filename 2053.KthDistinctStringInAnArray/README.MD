# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
I knew I had to use a hashmap to effective & quickly find the distinct values within the array

# Approach
<!-- Describe your approach to solving the problem. -->
* intialize counter = 0 and hashmap
* Make the array into a hashmap and keep track whether the values are distinct (bool). By iterating through every element in the array. If its in the hashmap already set it false meaning that its not distinct otherwise make it true if it is.
* Iterate through the hashmap and if the element is true increment the counter by one and if the counter is equal to k then return the key value
* If none works return ""


# Complexity
- Time complexity: O(N)
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: O(N)
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```
class Solution(object):
    def kthDistinct(self, arr, k):
        count = 0
        map = {}

        # Count occurrences of each string
        for item in arr:
            if item in map:
                map[item] = False  # Mark as not distinct
            else:
                map[item] = True  # Mark as distinct

        # Find the k-th distinct string
        for item in arr:
            if map[item]:  # Check if it's distinct
                count += 1
                if count == k:
                    return item
        return ""




        
```