# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None: return None

        # perform in-place dfs on root 
        self.dfs(root)

        # return root 
        return root

    def dfs(self, node: Optional[TreeNode]) -> Optional[TreeNode]:
        if node == None: return

        node.left, node.right = self.dfs(node.right), self.dfs(node.left)

        return node

# essentially, we want to switch every node's left and right child 
# if both left and right are null, we don't do anything
# if either left or right or both are non-null, we perform the switch 

# post-order traversal 