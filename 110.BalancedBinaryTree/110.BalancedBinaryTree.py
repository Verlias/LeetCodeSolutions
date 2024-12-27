# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node: Optional[TreeNode]) -> int:
            # Base case: If the node is None, its height is 0
            if not node:
                return 0
            
            # Recursively find the height of the left and right subtrees
            left_height = dfs(node.left)
            right_height = dfs(node.right)
            
            # If the subtree is already unbalanced, propagate -1 upwards
            if left_height == -1 or right_height == -1 or abs(left_height - right_height) > 1:
                return -1
            
            # Return the height of the current subtree
            return 1 + max(left_height, right_height)
        
        # Call dfs on the root; if the result is -1, the tree is unbalanced
        return dfs(root) != -1