# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict

# Approach 1: Nodes at same (x,y) are to be sorted: Using Map of Map of lists 
# Time Complexity: O(N) to Traverse + O(NLOGN) to Sort
# Space Complexity: O(N) for map + O(N) for queue

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
    
        # Map of map of lists -> {x:{y:[]}}
        # Outer Key: x coordinate
        # Inner Key: y coordinate
        # Value: List of nodes at same coordinates
        x_map = defaultdict(lambda: defaultdict(list))
        
        # Queue that stores (node,x,y)
        queue = [(root,0,0)]

        def level_order_traversal():
            while(queue):
                node_details = queue.pop(0)
                curr_node = node_details[0]
                x = node_details[1]
                y = node_details[2]
                
                # Append to x map
                x_map[x][y].append(curr_node.val)
                
                if curr_node.left:
                    # Append left node to Queue with (node, x-1, y+1)
                    queue.append((curr_node.left, x - 1, y + 1))
                if curr_node.right:
                    # Append right node to Queue with (node, x+1, y+1)
                    queue.append((curr_node.right, x + 1, y + 1))

        # Level order traversal takes care of values from top to bottom in one vertical           
        level_order_traversal()

        # Construct Traversal List from x map 
        # Sorted x values and y values to ensure top down and left right order of vertical traversal 
        traversal = [] 
        for i in sorted(x_map):
            y_map = x_map[i]
            combined_list = []
            for j in sorted(y_map):
                y_map[j].sort()  # sort nodes at same x and y
                combined_list += y_map[j]
            traversal.append(combined_list)

        return traversal

# Approach 2: Nodes at same (x,y) are not sorted: Using Map of lists 
# Time Complexity: O(N) to Traverse 
# Space Complexity: O(N) for map + O(N) for queue    

def verticalOrderTraversal(root):
    
    # Map to store x cordinates and their node values
    level_map = defaultdict(list)
    # Queue that stores (node,x,y)
    queue = [(root,0,0)]
    
    def level_order_traversal():
        while(queue):
            curr_node = queue.pop(0)
            # Append to level map
            level_map[curr_node[1]].append(curr_node[0].data)
            if curr_node[0].left:
                # Append left node to Queue with (node, x-1, y+1)
                queue.append((curr_node[0].left, curr_node[1] - 1, curr_node[2] + 1))
            if curr_node[0].right:
                # Append right node to Queue with (node, x+1, y+1)
                queue.append((curr_node[0].right, curr_node[1] + 1, curr_node[2] + 1))
    
    # Level order traversal takes care of values from top to bottom in one vertical           
    level_order_traversal()
    
    # Construct Traversal List from level map (sublists)
    # Start traversal of level map from min value of x  
    traversal = [] 
    min_x = min(level_map.keys())
    for i in range(min_x,len(level_map)):
        traversal += level_map[i]
    
    return traversal
    
	