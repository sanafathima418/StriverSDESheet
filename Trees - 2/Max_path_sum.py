# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Optimized Approach: Use same concept as diameter of BT
# Time Complexity: O(N) 
# Space Compelxity: O(1)

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = 0
        def find_max_path(node):
            nonlocal max_sum
            if not node:
                return 0
            
            # Keep going left or right until null
            # Only consider positive heights as taking negative heights, fails this case - [1,-2,3]
            lh = max(0, find_max_path(node.left))
            rh = max(0, find_max_path(node.right))
            # Calculate max path sum from sum seen for this node so far, not returned anywhere and only updated
            max_sum = max(max_sum,lh+rh+node.val)
            
            # When you reach end, add current node value to max height and return as left/right path sum
            return node.val + max(lh,rh)
        
        # For every node in tree traverse to calculate left and right heights
        find_max_path(root)
        return max_sum