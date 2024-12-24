# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0

        def inorder(root):
            if not root:
                return 0 

            left = inorder(root.left)
            right = inorder(root.right)
            self.diameter = max(self.diameter, left + right)
            return 1 + max(left, right)

        inorder(root)
        return self.diameter
        
        

        