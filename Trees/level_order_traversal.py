from os import *
from sys import *
from collections import *
from math import *

from sys import stdin, setrecursionlimit
from queue import Queue
setrecursionlimit(10**7)


#   Binary tree node class for reference
class BinaryTreeNode:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None

# ----------------------
def getLevelOrder(root):
    
    # Apporach: BFS traversal of Tree
    # Time Complexity:
    # Space Complexity:
    traversal = []
    queue = [root]
    
    def levelorder_traversal(node):
        while(queue): # Until queue not empty
            # 1. Pop element in front
            curr_node = queue.pop(0) 
            # 2. Append to Traversal
            traversal.append(curr_node.val)
            # 3. Push left node
            if curr_node.left:
                queue.append(curr_node.left)
            # 4. Push Right node
            if curr_node.right:
                queue.append(curr_node.right)
    
    # If tree exists
    if root:
        levelorder_traversal(root)
    
    return traversal
# ----------------------

#   Fast input
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


def printAns(ans):
    for x in ans:
        print(x, end=" ")
    print()


# main
T = int(stdin.readline().strip())
for i in range(T):
    root = takeInput()
    ans = getLevelOrder(root)
    printAns(ans)
