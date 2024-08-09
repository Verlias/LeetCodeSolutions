# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
* I knew that this question was a two pointer question because essentially the characters had to be sorted in a particular way in order for it to be right. I also knew that the two pointer algorithm would be useful in this case as it would allow me to compare every single character to eachother.

# Approach
<!-- Describe your approach to solving the problem. -->
* So, the first step that I took to solve this problem is firstly making a new string such that I could do the palindrome comparsion. This meant getting rid of all the spaces and non alphanumeric characters within the input string. I did this throuh the process of iterating through every character in the input and checking is it was alphanumeric. If it was then add that lower cased character to the new string.
* Once I had my new string, I proceeded to setup the two pointer variables... one at the first index and one at the last index of the new string. I did this through making first pointer = 0 and second pointer equal to the len(newstring) minus 1 so i could index it correctly.
* Then I made a while loop and essentially made it true until the first pointer goes past an index higher than the second pointer. This meant it would look over already saw characters or more so pass a midpoint.
* Then within this while loop it looks at every character using the two pointers. starting at the first pointer first index and the last index with the second pointer. So, for every time it found a character equal to eachother it would increment/decrement each pointer.
* Anything else return false
* if it follows through the whole while loop then return True that means all the phrase is palindrome.

# Complexity
- Time complexity: O(N)
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: O(N)
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```
class Solution(object):
    def isPalindrome(self, s):
        new_string = ""

        for i in s:
            if i.isalnum():
                new_string += i.lower()

        first_pointer = 0
        second_pointer = len(new_string) - 1

        #first_pointer is less than second pointer up untill it hits a midpoint or after
        while first_pointer < second_pointer:
            if new_string[first_pointer] == new_string[second_pointer]:
                first_pointer += 1
                second_pointer -= 1        
            else:
                return False

        return True

    

        
```