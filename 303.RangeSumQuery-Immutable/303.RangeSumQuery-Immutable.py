class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = []
        total = 0
        for i in nums:
            total += i
            self.prefix.append(total)
        

    def sumRange(self, left: int, right: int) -> int:
        prefix_right = self.prefix[right]
        if left > 0:
            prefix_left = self.prefix[left - 1]
        else:
            prefix_left = 0 
        return prefix_right - prefix_left


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)