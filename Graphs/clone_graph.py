"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from copy import deepcopy

class Solution:        
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        # Approach: Visited array stores node and its copy
        # Traverse node and create copy of each node and its neighbor
        # TC: O(N) for traversing all nodes
        # SC: O(N) for queue + O(N) for visited array
        
        visited = {}
        bfs_queue = []
        
        # Initialize new head and mark node as visited by storing its copy
        head = deepcopy(node) # head pointer for new graph
        
        if head:
            visited[node] = head
            bfs_queue.append(node)

            # BFS Traversal of graph
            while(bfs_queue):
                # 1. Get pointers of old and new graph for current node
                curr_node = bfs_queue.pop(0) # old graph pointer for current parent
                curr = visited[curr_node] # new graph pointer for current parent
                # 2. Traverse over all neighbors of curr node
                for neighbor in curr_node.neighbors:
                    if not neighbor in visited:
                        # 3. If neighbor is not visited then create copy and mark as visited
                        # CATCH: Creating deep copy copies its neighbors
                        new_neighbour = deepcopy(neighbor)
                        bfs_queue.append(neighbor)
                        visited[neighbor] = new_neighbour

        return head