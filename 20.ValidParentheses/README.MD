# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
I think the main thing that stood out to me when I had to solve this question is that I would some how figure out a way to see if brackets would be opened and closed. So, for example when I see that a open bracket is implemented on top of it would need to be a closing bracket and so on. So potentially I could use a stack to represent this

# Approach
<!-- Describe your approach to solving the problem. -->
* Make a stack array to keep track of the characters in the string
* iterate through the string. For everytime I see a opening bracket append it to the stack
* Assuming that there could be a a closer bracket I implement a elif statement to see if its a pair.
* Firstly check to make sure the closing bracket is not the first element in the stack.
* Afterwards check if its a pair.. if not return false. If so pop the opening bracket from the stack so we could check another pair.
* Once checking through every single element in the string check if the stack still has elements in it. If it does this means that there weren't valid parentheses as it wasnt able to pop the opening brackets away with a closing.


# Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for i in s:
            if (i == "(") or (i == "{") or (i == "["):
                stack.append(i)
            elif i in ")}]":
                if not stack:
                    return False
                if i == ")" and stack[-1] != "(":
                    return False
                if i == "}" and stack[-1] != "{":
                    return False
                if i == "]" and stack[-1] != "[":
                    return False
                stack.pop()
        
        return not stack
   




        
```