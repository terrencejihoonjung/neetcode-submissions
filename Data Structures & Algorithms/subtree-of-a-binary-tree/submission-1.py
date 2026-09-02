# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root: return False 
        if not subRoot: return True 
        
        if root.val == subRoot.val and self.dfs(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

# create dfs method that checks tree equality 
# iterate through root tree and run dfs method whenever values match. 

    def dfs(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p == None and q == None: return True
        elif (p == None or q == None): return False
        elif (p.val != q.val): return False
        else: return self.dfs(p.left, q.left) and self.dfs(p.right, q.right)