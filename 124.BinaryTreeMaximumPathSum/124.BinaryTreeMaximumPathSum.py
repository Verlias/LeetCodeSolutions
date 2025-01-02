# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]

        def dsf(root):
            #Compute Max Path Sum
            if not root:
                return 0
            
            leftmax = dsf(root.left)
            rightmax = dsf(root.right)
            leftmax = max(leftmax, 0)
            rightmax = max(rightmax, 0)

            res[0] = max(root.val + leftmax + rightmax, res[0])
            return root.val + max(leftmax, rightmax)


        dsf(root)
        return res[0]


        