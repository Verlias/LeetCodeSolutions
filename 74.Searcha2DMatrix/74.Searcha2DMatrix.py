class Solution(object):
    def searchMatrix(self, matrix, target):
        #Iterate through each item in the matrix
        for i in matrix:
            if not (i[0] <= target <= i[-1]):
                continue
            l = 0
            r = len(i) - 1
            while l <= r:
                mid = (r + l) // 2
                if i[mid] == target:
                    return True
                elif i[mid] < target:
                    l = mid + 1
                elif i[mid] > target:
                    r = mid - 1
            
        return False



