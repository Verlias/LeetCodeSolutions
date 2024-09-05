# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
I could sort and check if the strings are equal to each other. I could check the count of each key value of both strings and check if they are equal to each other.

# Approach
<!-- Describe your approach to solving the problem. -->
* HashTable Solution Quick Summary: Get the count of each character that appears in the string and compare between the two strings.
* Check if the len of both strings are equal or not. If not return False
* Create two dicts
* For loop in range of the len of either string (since we checked that they should be equal)
* Add each character as its key and keep track of its count
* Check if both dicts are equal to eachother (if distinct should be True)
* Sorting Solution: Sort the string and compare



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
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False

        c1 = {}
        c2 = {}

        for i in range(len(s)):
            c1[s[i]] = 1 + c1.get(s[i],0)
            c2[t[i]] = 1 + c2.get(t[i],0)
        
        return c1 == c2



        
```