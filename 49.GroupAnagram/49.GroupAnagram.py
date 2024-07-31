from collections import defaultdict


class Solution(object):
    def groupAnagrams(self, strs):
        hashmap = defaultdict(list) #Provides default value for non existent Keys

        for string in strs:
            sort_word = "".join(sorted(string))
            hashmap[sort_word].append(string)

        return list(hashmap.values())
            
        
'''
Thought Process:
Time Complexitiy:
'''