class Solution(object):
    def isPalindrome(self, s):
        new_string = ""

        for i in s:
            if i.isalnum():
                new_string += i.lower()

        first_pointer = 0
        second_pointer = len(new_string) - 1

        #first_pointer is less than second pointer up untill it hits a midpoint or after
        while first_pointer < second_pointer:
            if new_string[first_pointer] == new_string[second_pointer]:
                first_pointer += 1
                second_pointer -= 1        
            else:
                return False

        return True

        