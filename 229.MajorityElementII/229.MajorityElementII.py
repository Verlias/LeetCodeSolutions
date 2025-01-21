class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        #Not Optimal Solution uses O(2n) Time complexitity and O(2n) Space Comp
        hashset = {}
        for i in nums:
            hashset[i] = hashset.get(i,0) + 1


        res = []
        for i,j in hashset.items():
            if j > (len(nums) / 3):
                res.append(i)

        return res