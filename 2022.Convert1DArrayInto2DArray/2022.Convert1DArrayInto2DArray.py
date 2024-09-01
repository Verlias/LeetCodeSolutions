class Solution(object):
    def construct2DArray(self, original, m, n):
        if len(original) != m * n:
            return []

        res = [original[i:i + n] for i in range(0, len(original), n)]

        return res


'''
n is the number of elements in each row of the 2D array.
So it makes sense to get elements that span n elements at a time.
'''