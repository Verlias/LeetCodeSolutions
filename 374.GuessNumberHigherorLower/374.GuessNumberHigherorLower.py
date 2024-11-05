# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):

        l = 0
        r = n

        while l <= r:
            mid = l + (r - l) / 2
            if guess(mid) == 0:
                return mid
            elif guess(mid) > 0:
                l = mid + 1
            elif guess(mid) < 0:
                r = mid - 1


                