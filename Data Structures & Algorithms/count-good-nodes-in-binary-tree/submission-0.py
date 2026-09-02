# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0
        
        def dfs(node: Optional[TreeNode], path_max: int) -> None:
            if not node: return
            
            if node.val >= path_max: 
                self.count += 1

            dfs(node.left, max(path_max, node.val))
            dfs(node.right, max(path_max, node.val))
            
        dfs(root, root.val)
        return self.count