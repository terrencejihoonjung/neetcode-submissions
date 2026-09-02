# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []

        queue = collections.deque()
        queue.append(root)
        ans = []

        while queue:
            length = len(queue)
            curr = []

            for i in range(length):
                node = queue.popleft()
                curr.append(node.val)
                
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            
            if curr: ans.append(curr[-1])
        
        return ans
