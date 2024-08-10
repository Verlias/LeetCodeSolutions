class Solution(object):
    def finalValueAfterOperations(self, operations):
        hashmap = Counter(operations)
        value = 0
        for i, j in hashmap.items():
            if (i == "--X" or i == "X--"):
                value -= j
            elif (i == "X++" or i == "++X"):
                value += j
        return value
                
        