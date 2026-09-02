# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root)[1]
    
    def dfs(self, node: Optional[TreeNode]) -> (int, int):
        if node == None: return (0, 0) 

        l, ld = self.dfs(node.left)
        r, rd = self.dfs(node.right)

        d = max(ld, rd, l + r)
        return (max(l, r) + 1, d)
    
# If node is None: we return 0 
# At a given valid node: we return the max(l + 1, r + 1, l + r) 