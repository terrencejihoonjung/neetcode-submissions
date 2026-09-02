# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node: Optional[TreeNode]) -> (int, bool):
            if node == None: return (0, True)
            l_height, l_balanced = dfs(node.left)
            r_height, r_balanced = dfs(node.right)
            return (max(l_height, r_height) + 1, l_balanced and r_balanced and abs(l_height - r_height) <= 1)
        
        return dfs(root)[1]

# for a given node, check the difference between left and right height and check for balance
# dfs should return the height and whether the current node's left and right subtrees are balanced 