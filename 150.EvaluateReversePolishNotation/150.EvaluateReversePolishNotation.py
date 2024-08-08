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
