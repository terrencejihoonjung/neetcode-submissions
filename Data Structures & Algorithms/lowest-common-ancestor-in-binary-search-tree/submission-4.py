# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        return self.dfs(root,p, q)

    def dfs(self, node: Optional[TreeNode], p: TreeNode, q:TreeNode) -> Optional[TreeNode]:
        if not node: return None

        if (p.val <= node.val and q.val >= node.val) or (q.val <= node.val and p.val >= node.val):
            return node
        
        if p.val > node.val and q.val > node.val: return self.lowestCommonAncestor(node.right,p , q)
        return self.lowestCommonAncestor(node.left, p, q)
