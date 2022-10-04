from os import *
from sys import *
from collections import *
from math import *

'''
  ----Binary tree node class for reference-----
    class TreeNode:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None

'''

def getMaxWidth(root):

    # Apporach: BFS traversal of Tree
    # Time Complexity: O(N)
    # Space Complexity: O(N)
    
    # Queue consists of node,level
    queue = [(root,0)]
    
    # Map that stores number of nodes at each level
    # Map because it allows auto creation of keys that represent levels
    level_map = defaultdict(int)
    
    def levelorder_traversal(node):
        while(queue): # Until queue not empty
            # 1. Pop element in front
            node_details = queue.pop(0) 
            curr_node = node_details[0]
            curr_level = node_details[1]
            
            # 2. Add 1 against level in level map
            level_map[curr_level] += 1
            
            # 3. Push left node
            if curr_node.left:
                queue.append((curr_node.left, curr_level+1))
            # 4. Push Right node
            if curr_node.right:
                queue.append((curr_node.right, curr_level+1))
    
    # If tree exists
    if root:
        levelorder_traversal(root)
        
    max_len = 0
    # Calculate max length
    if level_map:
        max_len = max(level_map.values())
                             
    return max_len