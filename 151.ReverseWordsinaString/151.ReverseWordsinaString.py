class Solution:
    def reverseWords(self, s: str) -> str:
        res = s.split()
        result_string = " ".join(res[::-1])

        return result_string
        
        '''
        Two pointer Technique:
        Skip White Spaces 
        '''