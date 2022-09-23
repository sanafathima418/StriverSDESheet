# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Approach: Any traversal and check if values of node1.left == node2. right and node1.right == node2.left
# Important to check boundary conditions - if one node not available(return false) or both nodes not available(return true)
# Time Complexity: O(N) for traversal
# Space Complexity: O(1) 

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def preorder_traversal(node1, node2):
            # Boundary Conditions
            if not node1 and not node2:
                # If both nodes are leaf, then return True
                return 1
            elif (node1 and not node2) or (not node1 and node2):
                #
                return 0
            
            # Check if values not equal, immediately return False
            if node1.val != node2.val:
                return 0
            else:
                 # Propagate result of left and right subtree traversals
                if not preorder_traversal(node1.left,node2.right):
                    return 0
                if not preorder_traversal(node1.right,node2.left):
                    return 0
           
            # If no return so far, then valid mirror so return True
            return 1
        
        return preorder_traversal(root,root)