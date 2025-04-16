class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        #Hashset keeps track of unique freq
        hashset = set()
        #Dict to count freq 
        hashmap = {}
        #count freq
        for i in arr:
            hashmap[i] = 1 + hashmap.get(i,0)

        for key, value in hashmap.items():
            if value in hashset:
                return False
            hashset.add(value)

        return True        