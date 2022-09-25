# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # p and q both None: 
        if not p and not q: 
            return True 
        # one of p and q is None
        if not p or not q: 
            return False 
    
        #value is different
        if p.val != q.val: 
            return False 
        return self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left)
        
        
        