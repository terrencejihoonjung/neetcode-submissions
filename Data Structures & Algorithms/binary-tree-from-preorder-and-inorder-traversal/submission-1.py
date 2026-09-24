# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.p = 0
        self.nodes = {}
        for i in range(len(inorder)):
            self.nodes[inorder[i]] = i
        
        def build(start: int, end: int) -> Optional[TreeNode]:
            if start > end: return None
            
            new_node = TreeNode(preorder[self.p])
            idx = self.nodes[preorder[self.p]]

            self.p += 1
            
            new_node.left = build(start, idx - 1)
            new_node.right = build(idx + 1, end)

            return new_node
        
        return build(0, len(inorder) - 1)

# how do I rebuild? 
# - initialize root node and build from root 

# partition inorder using node in preorder
# - the left partition is the left subtree of that node
# - the right partition is the right subtree of that node 

# what do we do with the partitions? 
# - pass along the partitions with their respective "root" nodes as a subproblem
# - when the partition is empty, there are no nodes to build w/ -> return None

# use a variable to track which root node is being used
# fast look up would be nice for node in preorder to index of it in inorder 