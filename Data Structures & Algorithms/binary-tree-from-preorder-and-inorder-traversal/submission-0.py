# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.curr = 0
        self.p = preorder
        self.i = inorder
        self.n = len(inorder)

        self.nodes = {}
        for i in range(len(inorder)): 
            self.nodes[inorder[i]] = i
        
        def dfs(l: int, r: int) -> Optional[TreeNode]:
            if l > r: return None

            node = TreeNode(self.p[self.curr])
            pos = self.nodes[self.p[self.curr]]

            self.curr += 1

            node.left = dfs(l, pos - 1)
            node.right = dfs(pos + 1, r)

            return node

        return dfs(0, len(preorder) - 1)
        
# preorder gives us the parent node first 
# inorder gives us the left node first 

# what information do we get with both preorder and inorder 
#   - for a given node in preorder, we can partition inorder on that node 
#     to see the left and right subtrees 

# each partitio of inorder becomes a subproblem we solve 
# if there's nothing on the left and right parititions for a given node, we reached a leaf node 

# map value in preorder to index of value in inorder first