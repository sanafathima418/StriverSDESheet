class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        from collections import defaultdict, Counter
        
        # Approach: Compare adjacent words and generate adjlist, then Topo Sort BFS using Kahn's Algorithm
        # TC: O(V+E) for traversing all edges and vertices
        # SC: O(V) for queue, indegree, adj_list
        
        adj_list = defaultdict(list)
        indegree = {}
        bfs_queue = []
        traversal = ""

        # 1. Initialize adj list with all nodes and update indegree array
        # There is unnecessary complication if this is done after STEP2
        # Some nodes get missed in either of the arrays
        # Can be avoided if 2.1 is replaced with a zip for word1 and 2
        for word in words:
            for char in word:
                if char not in indegree:
                    adj_list[char] = []
                    indegree[char] = 0
        
        # 2. Populate adj list with all edges and update indegree array
        # Compare 2 words at a time
        for i in range(len(words)-1):
            # 2.1. Get min length to traverse over 2 words
            min_len = min(len(words[i]),len(words[i+1]))
            for j in range(min_len):
                # 2.2 For first mismatch update adjlist and indegree and break
                if words[i][j] != words[i+1][j]:
                    adj_list[words[i][j]].append(words[i+1][j])
                    indegree[words[i+1][j]] += 1
                    break
                # 2.3 Special test case where x = abc and y = ab  
                # When all chars of one string match with the other, the shorter string to be before else invalid test case
                # Order not possible so return immediately
                if j == min_len-1 and len(words[i]) > len(words[i+1]):
                    return ""
        
        # 3. Loop over all nodes to check for start points
        for node in adj_list:
            if indegree[node] == 0:
                bfs_queue.append(node)
        
        # 4. BFS Traversal
        while(bfs_queue):
            curr_node = bfs_queue.pop(0)
            traversal += curr_node
            
            # 4.1 Traverse over adj nodes
            for adj_node in adj_list[curr_node]:
                # 4.2 Reduce indegree count
                indegree[adj_node] -= 1
                # 4.3 If indegree has reduced to zero then push to queue
                if indegree[adj_node] == 0: 
                    bfs_queue.append(adj_node)

        # 5. If all nodes traversed then no cycle so possible to complete all courses
        # print(traversal)
        if len(traversal) == len(indegree):
            return traversal
        return ""
