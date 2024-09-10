class Solution(object):
    def longestOnes(self, nums, k):
        l = 0
        r = 0
        best_max = 0 
        count_of_zeros = 0

        #Iterate through Array
        while r < len(nums):
            #Keeps Track of the Count of zeros pasted
            if nums[r] == 0:
                count_of_zeros += 1
            
            while count_of_zeros > k:
                #Process Window
                best_max = max(best_max, r - l )
                #Contract Window
                if nums[l] == 0:
                    count_of_zeros -= 1
                l += 1
            #Expands Window
            r += 1
        #Edge Case
        if count_of_zeros <= k:
            best_max = max(best_max, r - l)

        return best_max
            
