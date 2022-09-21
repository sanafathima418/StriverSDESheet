from os import *
from sys import *
from collections import *
from math import *

from sys import stdin, setrecursionlimit
from queue import Queue
setrecursionlimit(10**7)

# Following is the TreeNode class structure:
class BinaryTreeNode:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None

def getTopView(root):
        # Approach: Vertical Order Traversal + only get nodes on top of each vertical level
        # Time Complexity: O(N) for Traversal + O(NLOGN) for Sorting
        # Space Complexity: O(N) for Map + O(N) for Queue
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
        traversal = [] 
        if root:
            level_order_traversal()
            # Construct Traversal List from x map 
            # Sorted x values and y values to ensure top down and left right order of vertical traversal 
            for i in sorted(x_map):
                all_y = list(x_map[i].keys())
                j = min(all_y)
                sub_list = x_map[i][j]
                traversal.append(sub_list[-1])

        return traversal

# Taking input.
def takeInput():

    arr = list(map(int, stdin.readline().strip().split(" ")))

    rootData = arr[0]

    n = len(arr)

    if(rootData == -1):
        return None

    root = BinaryTreeNode(rootData)
    q = Queue()
    q.put(root)
    index = 1
    while(q.qsize() > 0):
        currentNode = q.get()

        leftChild = arr[index]

        if(leftChild != -1):
            leftNode = BinaryTreeNode(leftChild)
            currentNode.left = leftNode
            q.put(leftNode)

        index += 1
        rightChild = arr[index]

        if(rightChild != -1):
            rightNode = BinaryTreeNode(rightChild)
            currentNode .right = rightNode
            q.put(rightNode)

        index += 1

    return root

# Printing the tree nodes.
def printAns(ans):
    for x in ans:
        print(x, end=" ")
    print()


# Main.
T = int(stdin.readline().strip())
for i in range(T):
    root = takeInput()
    ans = getTopView(root)
    printAns(ans)