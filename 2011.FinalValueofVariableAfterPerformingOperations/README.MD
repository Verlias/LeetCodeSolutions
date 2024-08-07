# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
I knew I could get the number of times I would have to add or subtract by keeping a counter of the frequencies of an element. Then I would be able to return a value based on the number of apperances of those particular elements.

# Approach
<!-- Describe your approach to solving the problem. -->
* I made a counter that got the frequencies of all the elements.
* I iterated over the items within the hashmap.
* If the key equaled to either one of the elements It would add or subtract based on the key value pair then finally return its result.


# Complexity
- Time complexity: O(N)
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```
class Solution(object):
    def finalValueAfterOperations(self, operations):
        hashmap = Counter(operations)
        value = 0
        for i, j in hashmap.items():
            if (i == "--X" or i == "X--"):
                value -= j
            elif (i == "X++" or i == "++X"):
                value += j
        return value
                
        



        
```