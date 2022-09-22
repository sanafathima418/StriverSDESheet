# Approach: Inorder Traversal + Backtracking
# Time Complexity: O(N)
# Space Complexity: O(N)

def root_to_node(root,end_node):

    traversal = []
        
    def inorder(node,end_node):
        # If no nodes left to traverse, then node not found so return 0
        if node == None:
            return 0

        # Append to traversal list and check if current node is the end node, if found return 1
        traversal.append(node)
        if node.val == end_node.val:
            return 1

        # If the left and right traversals are successful, propagate 1    
        if inorder(node.left,end_node) or inorder(node.right,end_node):
            return 1

        # If search not successful in left and right traversals, not found so pop and return 0   
        traversal.pop()
        return 0

    inorder(root,end_node)
    return traversal