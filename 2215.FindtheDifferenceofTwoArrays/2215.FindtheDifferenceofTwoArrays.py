class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        hashset_num1 = set(nums1)
        hashset_num2 = set(nums2)
        res = []
        res_1 = []
        res_2 = []

        for i in nums1:
            if i not in hashset_num2:
                if i not in res_1:
                    res_1.append(i)

        for i in nums2:
            if i not in hashset_num1:
                if i not in res_2:
                    res_2.append(i)
        
        res.append(res_1)
        res.append(res_2)
        return res



        