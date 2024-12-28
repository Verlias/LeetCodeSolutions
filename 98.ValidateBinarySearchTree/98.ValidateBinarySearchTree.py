# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        res = []
        def dfs(root):

            if not root:
                return
                
            dfs(root.left)
            if not res or root.val >= res[-1]:
                res.append(root.val)
            elif root.val <= res[-1]:
                res.append(root.val)
           
            dfs(root.right)
            
    
        dfs(root)
        count = set()
        for i in res:
            if i in count:
                return False
            count.add(i)
            

        return sorted(res) == res