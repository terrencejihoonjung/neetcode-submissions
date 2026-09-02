# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []

        queue = collections.deque()
        queue.append(root)
        ans = []

        while queue:
            l = len(queue)
            curr = []

            for i in range(l):
                node = queue.popleft()
                curr.append(node.val)
                
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            
            ans.append(curr)

        return ans

# worst case the queue's size the # of leaf nodes 
