class Solution(object):
    def isAnagram(self, s, t):
        #could just do  sorted(s) == sorted(t)
        if (''.join(sorted(s))) == (''.join(sorted(t))):
            return True
        else:
            return False
        
        

'''
Thought Process:
Time Complexitiy: O(NLogN)

'''