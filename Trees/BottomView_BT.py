from os import *
from sys import *
from collections import *
from math import *

from sys import stdin, setrecursionlimit
import queue
import sys
from collections import OrderedDict
setrecursionlimit(10**6)


# Following is the structure used to represent the Binary Tree Node.
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Approach: Vertical Order Traversal + only get nodes on bottom of each vertical level
# Time Complexity: O(N) for Traversal + O(NLOGN) for Sorting
# Space Complexity: O(N) for Map + O(N) for Queue
	
def bottomView(root):
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
                x_map[x][y].append(curr_node.data)
                
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
            all_y = list(x_map[i].keys())
            j = max(all_y)
            sub_list = x_map[i][j]
            traversal.append(sub_list[-1])

        return traversal


# Taking level-order input using fast I/O method.
def takeInput():
    levelOrder = list(map(int, stdin.readline().strip().split(" ")))
    start = 0

    length = len(levelOrder)

    if length == 1:
        return None

    root = BinaryTreeNode(levelOrder[start])
    start += 1

    q = queue.Queue()
    q.put(root)

    while not q.empty():
        currentNode = q.get()

        leftChild = levelOrder[start]
        start += 1

        if leftChild != -1:
            leftNode = BinaryTreeNode(leftChild)
            currentNode.left = leftNode
            q.put(leftNode)

        rightChild = levelOrder[start]
        start += 1

        if rightChild != -1:
            rightNode = BinaryTreeNode(rightChild)
            currentNode.right = rightNode
            q.put(rightNode)

    return root


# Main.
t = int(input())
while t:
    root = takeInput()
    answer = bottomView(root)
    print(*answer)
    t = t - 1
