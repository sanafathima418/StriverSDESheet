# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Approach: Level Order Traversal(level-wise) and flip 
# Time Complexity: O(N)
# Space Complexity: O(N) + O(N)

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        queue = [root]
        traversal = []
        
        def level_order_traversal():
            
            while(queue):
                # Get length of queue that denotes number of nodes at current level
                curr_len = len(queue)
                
                sub_list = []
                while(curr_len): # For every level
                    # Pop all nodes at current level and append to traversal list
                    curr_node = queue.pop(0)
                    sub_list.append(curr_node.val)
                    
                    # Push child nodes of popped node
                    if curr_node.left: 
                        queue.append(curr_node.left)
                    if curr_node.right:
                        queue.append(curr_node.right)
                        
                    curr_len -= 1
                # After each level, append all nodes at level to main list
                traversal.append(sub_list)
        
        if root:
            level_order_traversal()
        
        # Reverse even indices for zig zag order
        n = 1
        for i,inner_list in enumerate(traversal):
            if n%2 == 0:
                traversal[i] = inner_list[::-1] # flip
            n += 1
        
        return traversal
            
            
            