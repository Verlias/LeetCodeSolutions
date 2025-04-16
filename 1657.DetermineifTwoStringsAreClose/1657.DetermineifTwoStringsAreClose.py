class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        
        hashmap_1 = {}
        hashmap_2 = {}

        for i in word1:
            hashmap_1[i] = 1 + hashmap_1.get(i,0)
        
        for i in word2:
            hashmap_2[i] = 1 + hashmap_2.get(i,0)
        
        if set(hashmap_1.keys()) != set(hashmap_2.keys()):
            return False
            
        return Counter(hashmap_1.values()) == Counter(hashmap_2.values())
        