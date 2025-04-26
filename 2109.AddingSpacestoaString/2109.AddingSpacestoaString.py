class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        
        pointer = 0
        string = ""
        for char in range(0,len(s)):
            if (pointer != len(spaces)):
                if spaces[pointer] == char:
                    string += " "
                    pointer += 1
            string += s[char]
        return string



        