# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node: Optional[TreeNode], left: float, right: float) -> bool:
            if not node: return True

            l = dfs(node.left, left, node.val)
            r = dfs(node.right, node.val, right)

            return left < node.val < right and l and r 
        
        return dfs(root, float("-inf"), float("inf"))

