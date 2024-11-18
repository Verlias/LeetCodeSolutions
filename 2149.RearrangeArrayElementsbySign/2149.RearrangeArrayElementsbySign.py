class Solution(object):
    def rearrangeArray(self, nums):
        pos_arr = []
        neg_arr = []
        res = []
        for i in nums:
            if i < 0:
                neg_arr.append(i)
            else:
                pos_arr.append(i)

        
        #Two Pointer
        pos_ptr = 0
        neg_ptr = 0
        #Equal number of both pos and neg
        while pos_ptr <= len(pos_arr) - 1 and neg_ptr <= len(neg_arr) - 1:
            res.append(pos_arr[pos_ptr])
            res.append(neg_arr[neg_ptr])
            pos_ptr += 1
            neg_ptr += 1

        return res


