from collections import defaultdict

# Approach: Traverse over colors to check if possible, if yes propagate True else check other options
# Time Complexity: O(N^M) for n nodes we check m possibilities
# Space Complexity: O(N) for color array + O(N) Auxiliary Space

def graphColoring(mat,m):
    
    # Create Adjacency List - To check colors possible in check_possible
    adj_list = defaultdict(list)
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] == 1:
                adj_list[i].append(j)
    
    # Check if possible to color node with said color
    color_array = [0] * len(mat)
    def check_possible(node,color):
        for adj_node in adj_list[node]:
            if color_array[adj_node-1] == color:
                return False
        return True
    
    # BackTrack
    def backtrack(node):
        # 1. Base Case
        if node == len(mat):
            return True
        
        # 2. Traverse over colors
        for color in range(1,m+1):
            if check_possible(node,color):
                # 3. Assign Color
                color_array[node-1] = color
                if backtrack(node+1):
                    # 4. Check next node and propagate True if colors worked
                    return True
                # 5. If colors didn't work, unassign
                color_array[node-1] = 0    
        # No back propagation from step 4 so not possible
        return False
    
    # Colors nodes with backtracking one by one (0-N and not as per adj_list) 
    if backtrack(0):
        return "YES"
    return "NO"


