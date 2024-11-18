class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        new_string = ""
        for i in word1:
            new_string += i

        new_string2 = ""
        for i in word2:
            new_string2 += i

        return new_string == new_string2
