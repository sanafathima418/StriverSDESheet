# Approach: Level Order Traversal and for every node, push index as 2i+1 for left and 2i+2 for right
# Time Complexity: O(N)
# Space Complexity: O(N)

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        # Queue which stores a tuple which is node and index of node(to be assigned)
        queue = [(root,0)]
        max_width = 1
            
        while(queue):
                curr_len = len(queue)
                
                # For current level nodes calculate width and compare with max width
                first = queue[0][1]
                last = queue[-1][1]
                curr_level_len = (last - first) + 1
                max_width = max(max_width,curr_level_len)
                
                # Level Order Traversal 
                while(curr_len):
                    curr_node = queue.pop(0)
                    if curr_node[0].left:
                        # Append Left
                        queue.append((curr_node[0].left,(2*curr_node[1])+1))
                    if curr_node[0].right:
                        # Append right
                        queue.append((curr_node[0].right,(2*curr_node[1])+2))
                    
                    curr_len -= 1
        
        return max_width