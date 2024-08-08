# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
* Just a personal note. It always seems as though you can identify a stack problem where there has to be come sort of order something has to go in.
* In this case of the question I needed to add numbers in a particular way such that I could get the result, so I knew I had to use a stack. That being said noticing I had to add numbers to a stack no many how many numbers are on the stack i needed to use the two on the top paired with an operator to add to a value.


# Approach
<!-- Describe your approach to solving the problem. -->
* I firstly made a numberArray = [] to keep track of the current numbers in the stack. -- Eventually once it goes through all of the tokens the only number in there would be the result.
* Firstly iterate through all the elements in tokens. If its a number append it to the numberArray stack and if its a operator we could go onto doing the operations. We could assume that by the time a operator pops up there are already two numbers in the stack.
* Once we hit a operator we want to pop the two numbers on the top of the stack and use them as numbers to work with based on the operator.
* If adding do x + y ... etc
* once we have the value from using the two numbers and the operator the stack is cleared so we want to append that value
* Then we use that appended value to be later used in the equation. (acting potentially as a x or y)
* then once we combine all the numbers together eventually we should have one singular element in the stack which is our result.

# Complexity
- Time complexity: O(N)
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```
class Solution(object):
    def evalRPN(self, tokens):
        numberArray = []
        
        for i in tokens:
            if i not in "+-*/":
                numberArray.append(int(i))
            else:
                y = numberArray.pop()
                x = numberArray.pop()
                
                if i == '+':
                    value = x + y
                elif i == '-':
                    value = x - y
                elif i == '*':
                    value = x * y
                elif i == '/':
                    value = int(float(x) / y)
                
                numberArray.append(value)
        
        return numberArray[-1]
        
```