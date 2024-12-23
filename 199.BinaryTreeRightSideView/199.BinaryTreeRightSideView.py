# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result_before = []
        queue = deque()
        
        if root:
            queue.append(root)

        while len(queue) > 0:
            res_inner = []
            for i in range(len(queue)):
                curr = queue.popleft()
                res_inner.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            result_before.append(res_inner)
        
        res_final = []
        for i in result_before:
            if len(i) == 0:
                return []
            elif len(i) == 1:
                res_final.append(i[0])
            else:
                res_final.append(i[-1])
        
        return res_final


        
        