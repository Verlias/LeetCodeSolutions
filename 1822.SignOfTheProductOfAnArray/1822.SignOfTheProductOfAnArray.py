class Solution(object):
    def arraySign(self, nums):
        
        #Get Product given integer Array
        product = 1
        for i in range(len(nums)):
            product *= nums[i]

        def signFunc(product):
            if product == 0:
                return 0
            elif product > 0:
                return 1
            elif product < 0:
                return -1
 

        return signFunc(product)

