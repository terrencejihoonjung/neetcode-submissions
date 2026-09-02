# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []

        nodes = [root]
        ans = []

        while nodes:
            length = len(nodes)
            level = []
            next_level = []

            for i in range(length):
                curr = nodes[i]
                level.append(curr.val)
                
                if curr.left: next_level.append(curr.left)
                if curr.right: next_level.append(curr.right)
            
            ans.append(level)
            nodes = next_level

        return ans
