
# Binary tree node class for reference
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Naive Approach: Add left height and right height of current node and compare against max height 
# Time Complexity: O(N^2) as for every node we call height function 
# Space Compelxity: O(1)

def diameterOfBinaryTree(root):
        max_height = 0

        def find_height(node):
            # DFS Approach
            if not node:
                return 0
            
            # Caclculate left and right heights by returning max of lh and rh + 1
            lh = find_height(node.left)
            rh = find_height(node.right)
            # For every level down add 1 to the heights
            return 1 + max(lh, rh)
        
        def traverse(node):
            nonlocal max_height
            if not node:
                return 0
            
            # Get current_height/diameter by adding left and right heights of current node
            curr_height = find_height(node.left) + find_height(node.right)
            
            max_height = max(max_height, curr_height) # Calculate max height
            
            # Traverse the left subtree
            traverse(node.left)
            # Traverse the right subtree
            traverse(node.right)
        
        # For every node in tree traverse to calculate left and right heights
        traverse(root)
        return max_height

# Optimized Approach: Use post order traversal to calculate diameter and height in one go
# Time Complexity: O(N) 
# Space Compelxity: O(1)
# note: Optimzed solution not the most intuitive, watch video to understand
        max_height = 0
        def find_diameter(node):
            nonlocal max_height
            if not node:
                return 0
            
            # Keep going left or right until null
            lh = find_diameter(node.left)
            rh = find_diameter(node.right)
            # Calculate max height from height seen for this node so far, not returned anywhere and only updated
            max_height = max(max_height,lh+rh)
            
            # When you reach end, add one to max height and return as left/right height
            return 1 + max(lh,rh)
        
        # For every node in tree traverse to calculate left and right heights
        find_diameter(root)
        return max_height

