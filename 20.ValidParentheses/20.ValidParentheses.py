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
   

