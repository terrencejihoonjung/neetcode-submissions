# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node: Optional[TreeNode], l: int, r: int) -> bool:
            if not node: return True
            if node.val <= l or node.val >= r: return False 
            return dfs(node.left, l, min(r, node.val)) and dfs(node.right, max(l, node.val), r)
        return dfs(root, float("-inf"), float("inf"))
        
    

# left is less than curr, right is greater than curr

#    3
# 1       4
#    2

# need to know parent node values, specifically most recent left/right parent  
# we should track the max of the left parent and the min of the right parent 
# use dfs and as we go down check whether current node's val is valid 
# if null node is reached, return True 