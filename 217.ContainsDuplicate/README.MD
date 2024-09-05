# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
Compare the current number thats being looked at by some other number or group

# Approach
<!-- Describe your approach to solving the problem. -->
* Two Sentence Summary: Make a hashset to check whether or not there are distinct numbers vs not. Return True/False
* Make a Hashset
* Iterate through the list and add each distinct number to the hashset. If a number appears thats already in the hashset return True. Otherwise False.


# Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->
O(N)

- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
O(N)

# Code
```
class Solution:
    def containsDuplicate(self, nums):
        hashset = set()
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False



Faster Solution: Checking whether all numbers are distinct by seeing if the len of the hashset of the nums list is equal to the original
class Solution:
    def containsDuplicate(self, nums):
        return len(set(nums)) != len(nums)



        
```