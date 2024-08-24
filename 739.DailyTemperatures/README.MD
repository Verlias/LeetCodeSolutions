# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->\
* I saw that I need to transverse the array and be done once. (In my personal experience, It seems as though if i want a efficent algorithm and only transverse the array once. I typically would use a stack to do so).
* What lead me to the assumption that I needed a monotonic stack was really the fact that I needed to have the comparsion of each element in terms of value at each step.

# Approach
<!-- Describe your approach to solving the problem. -->
* Summarize how to solve in two sentences: You want to use a stack that keeps tracks of your current index and initalize your result array to be equal to zero. Then loop through the array and everytime you find a value thats greater than the top number of the stack append it to the specific location in the result array and make the value be minus your current index and stack index.
* Intialize a stack that keeps track of each index value in the temperature array. And Result array as all zeros times the len of your temp array
* Then loop through the whole array going by indexes of your array.
* append each index to your stack after your while loop
* while loop checking if theres anything in the stack and if the current index value is greater than the top of your stack then run
* pop the stack and get that value and represent it as your index value
* append your result to that specific index value and make it equal to the current loop iteration minus the popped stack value.

# Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```
class Solution(object):
    def dailyTemperatures(self, temperatures):
        stack = []
        result = [0] * len(temperatures) 

        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                index = stack.pop()
                result[index] = i - index
            stack.append(i)
        return result

        
```