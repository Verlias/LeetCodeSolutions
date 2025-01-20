class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        hashset = set(jewels)
        count = 0
        for i in stones:
            if i in hashset:
                count += 1
        return count        


        