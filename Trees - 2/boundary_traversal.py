from os import *
from sys import *
from collections import *
from math import *

# Following is the Binary Tree node structure:
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def traverseBoundary(root):
    traversal_stack = []
    right_traversal_stack = []

    def left_traversal(node):
        if not node.left and not node.right:
            return 1
        traversal_stack.append(node.data)
        if node.left:
            if left_traversal(node.left):
                return 1
        elif node.right:
            if left_traversal(node.right):
                return 1

    def leaf_nodes(node):
        if not node.left and not node.right:
            traversal_stack.append(node.data)
            return 
        if node.left:
            leaf_nodes(node.left)
        if node.right:
            leaf_nodes(node.right)

    def right_traversal(node):
        if not node.left and not node.right:
            return 1
        right_traversal_stack.append(node.data)
        if node.right:
            if right_traversal(node.right):
                return 1
        elif node.left:
            if right_traversal(node.left):
                return 1

    if root:
        traversal_stack.append(root.data)
        if root.left:
            left_traversal(root.left)
        if root.left or root.right:
            leaf_nodes(root)
        if root.right:
            right_traversal(root.right)
        
        traversal_stack += right_traversal_stack[::-1]
        
    return traversal_stack
