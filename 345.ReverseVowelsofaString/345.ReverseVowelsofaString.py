class Solution:
    def reverseVowels(self, s: str) -> str:
        string = list(s)
        l = 0
        r = len(string) - 1

        while l <= r:
            if string[l].lower() in 'aeiou' and string[r].lower() in 'aeiou':
                string[l], string[r] = string[r], string[l]
                l += 1
                r -= 1
            elif (string[l].lower() not in 'aeiou'):
                l += 1
            elif (string[r].lower() not in 'aeiou'):
                r -= 1

        return "".join(string)


        