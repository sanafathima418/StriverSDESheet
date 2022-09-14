def solveNQueens(n):
     # Approach: Traverse over matrix column by column and loop over rows for possibilities to check if possible
    # Time Complexity: O(N!^N) for N nodes we check N! possibilities
    # Space Complexity: O(N) Auxiliary Space
    
    matrix = [[0 for i in range(n)] for j in range(n)] 
    main_list = []
    
     # Check if possible to place queen at row and column
    def check_possible(row,col):
        
        # 1. Check row to left only, as right is unexplored
        for i in range(col):
            if (matrix[row][i]):
                return False
            
        # 2. Check left diagonal
        i = row
        j = col
        while(i >=0 and j >= 0):
            if (matrix[i][j]):
                return False
            i -= 1
            j -= 1
        
        # 3. Check left anti-diagonal
        i = row
        j = col
        while(i < n and j >= 0):
            if (matrix[i][j]):
                return False
            i += 1
            j -= 1
        
        # No need to check col(up,down), row(right), diagonal(right), anti-diagonal(right) as none of these are explored 
        return True
        
        
    # BackTrack
    def backtrack(col):
        if col == n:
            # Flatten Matrix as meed to return matrix as 1d
            flatten_list = [k for sub in matrix for k in sub]
            if flatten_list not in main_list:
                if sum(flatten_list) == n:
                    # If number of queens == n given by sum as every queen is marked by 1
                    main_list.append(flatten_list)
            return 
        
        # As we are checking one col at a time, possibilities are places to place Queens at which will be rows
        for row in range(n):
            if check_possible(row,col):
                matrix[row][col] = 1 # Assign
                backtrack(col+1)  # Place queen only once in a col, hence if placed move to next col
                matrix[row][col] = 0 # Unassign       
    
    # Traverse over board, column by column
    backtrack(0)
    return main_list

