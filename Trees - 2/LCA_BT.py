# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Approach 1(Brute Force): DFS to find paths from root to p and q
        # Time Complexity: O(N) 
        # Space Complexity: O(N) + O(N) for the two traversal lists  
        traversal = []
        
        def inorder(node,end_node):
            if node == None:
                return 0
            
            traversal.append(node)
            if node.val == end_node.val:
                return 1
            
            if inorder(node.left,end_node) or inorder(node.right,end_node):
                return 1
            
            traversal.pop()
            return 0
        
        
        inorder(root,p)
        list_p = traversal.copy()
        traversal = []
        inorder(root,q)
        list_q = traversal.copy()
        
        i = 0
        while(i < len(list_p) and i < len(list_q)):
            if list_p[i].val != list_q[i].val:
                break
            i += 1
        return list_p[i-1]

        # Approach 2: InOrder Traversal to Optimize Space
        # 1. if left and right -1, then return -1 
        # 2. if left -1, return right
        # 3. if right -1. return left
        # 4. IMP: if left and right subtree return non -1 then return node
        # Time Complexity: O(N) 
        # Space Complexity: O(1)

        end_nodes = [p,q]
        
        def inorder(node):
            # If reached end, return not found -1
            if node == None:
                return -1
            
            # If curr node is one of searched, return node
            if node in end_nodes:
                return node
            
            # Traverse left and right subtrees
            la = inorder(node.left)
            ra = inorder(node.right)
            
            # If not match in either return -1
            if la == -1 and ra == -1: 
                return -1
            elif la == -1:
                return ra # right return matched
            elif ra == -1:
                return la # left return matched
            
            # If both return non -1 then return current node as it is the lca
            return node
     
        return inorder(root)

