# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.vals = []

        def inorder(node: Optional[TreeNode]) -> None:
            if not node: return
            inorder(node.left)
            self.vals.append(node.val)
            inorder(node.right)

        inorder(root)
        return self.vals[k-1]


# get values from an in-order traversal and return the (k-1)th element -> O(n)
# get kth value during in-order traversal -> O(k)