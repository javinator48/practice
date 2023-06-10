# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #Hypothesis, since a tree with the same structure will have the same order from the node. We use in-order traversal to traverse both trees and compare the orders of the visits. 
        if not p and not q: 
            return True
        if  not q or not p: 
            return False
        if p.val != q.val: 
            return False 
        return self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left)