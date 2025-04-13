class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0
        hashset = set(allowed)
        
        for word in words:
            consistent = True
            for char in word:
                if char not in hashset:
                    consistent = False
                    break
            if consistent:
                count += 1
        return count

        