# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
I knew there needed to be some way that I could keep track of the minimum values that i append to the stack

# Approach
<!-- Describe your approach to solving the problem. -->
* Make a stack and minStack array
* For everytime I push an item to the stack. I would also check if its less than the value at the top of the minStack. If theres nothing in the minStack append it then.
* Whenever I pop an item I would first check if its possible (by checking if theres anything in the stack). if so then pop then check if i popped the minimum value from the stack by comparing in the minStack.
* Then return[-1] for minStack to get the min value.
* Idea is that the min value always stays at the end of the array or more so top.

# Complexity
- Time complexity: O(1)
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: O(N)
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```
class MinStack(object):

    def __init__(self):
        self.stack = []
        self.minStack = [] #Keeps Track of the Minimum Values in the Stack
        

    def push(self, val):
        self.stack.append(val)

        #If the minstack is empty then append val to it. If the top value on the minstack is greater than the incoming append the new value to the minstack
        if not self.minStack or val <= self.minStack[-1]:
            self.minStack.append(val)

        
    def pop(self):
        if self.stack:
            x = self.stack.pop()

            if x == self.minStack[-1]:
                self.minStack.pop()

        

    def top(self):
        return self.stack[-1]
        

    def getMin(self):
        return self.minStack[-1]


        
```