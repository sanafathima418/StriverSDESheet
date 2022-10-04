# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Approach: Any traversal, swap left and right nodes for every node in tree, If no node or leaf return
# Time Complexity: O(N) for preorder traversal
# Space Complexity: O(1)

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def swap(a,b):
            tmp = a
            a = b
            b = tmp
            return a,b
        
        
        def invert(node):
            # If no node, return
            if not node:
                return 
            
            # If leaf node, return
            if not node.left and not node.right:
                return 
            
            # Swap left and right nodes
            node.left,node.right = swap(node.left,node.right)
            
            # Traverse left and right nodes
            invert(node.left)
            invert(node.right)
            
        if root:    
            invert(root)
        return root
            