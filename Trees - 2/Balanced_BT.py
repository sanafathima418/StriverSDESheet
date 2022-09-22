# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Approach: Use same concept of finding diameter of tree to calculate left and right heights
# Time Complexity: O(N) for post order traversal
# Space Complexity: O(1)

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # If balanced some number is returned, else -1
        def find_height(node):
                if not node:
                    return 0
                
                # Keep going left or right until null
                # If either height is -1 then not balanced so return 
                lh = find_height(node.left)
                if lh == -1:
                    return -1
                
                rh = find_height(node.right)
                if rh == -1: 
                    return -1
            
                # Check difference in heights of left and right subtree and if > 1 unset check_balanced
                if (abs(lh-rh)) > 1:
                    return -1

                # When you reach end, add one to height and return as left/right height
                return 1 + max(lh,rh)
        
        # For every node in tree traverse to calculate left and right heights
        if find_height(root) == -1:
            return 0
        return 1