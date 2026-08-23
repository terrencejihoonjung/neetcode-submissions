# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None: return 0
        return self.dfs(root, 0)
    
    def dfs(self, node: Optional[TreeNode], depth: int) -> int:
        if node == None: return 0
        return max(self.dfs(node.left, depth + 1), self.dfs(node.right, depth + 1)) + 1

        
# run dfs on the root and track longest depth 
# as we traverse, we increment the current depth 
# we also track the max depth and propogate it up in the call stack 

# if we are at a leaf node's children, we return 0 
# at any other node, we return the (max depth between the left and right sub trees) + 1