# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        
        root = TreeNode(preorder[0])
        #Seperates the root node between the left and right subtree for inorder 
        mid = inorder.index(preorder[0])
        #Recursion
        root.left = self.buildTree(preorder[1:mid + 1],inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1:],inorder[mid + 1:])
        return root
        


        