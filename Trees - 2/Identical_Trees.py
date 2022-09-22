# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Approach: Any traversal works - used inorder
# Time Complexity: O(N) - traversing 2 trees at same time
# Space Complexity: O(1)

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def check_trees(nodep, nodeq):
            
            # If null in any, check if values are same 
            if not nodep or not nodeq:
                return (nodep == nodeq)
            
            # If current nodes not equal return immediately
            if nodep.val != nodeq.val:
                return 0
            
            # If subtrees return not equal propagate 
            if not check_trees(nodep.left,nodeq.left) or not check_trees(nodep.right,nodeq.right):
                return 0
            
            # All good so identical trees
            return 1
        
        return check_trees(p,q)