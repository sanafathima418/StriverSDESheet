def isItSudoku(matrix):
    
    # Approach: Traverse over whole board to check if possible to place digits 1-9, if yes propagate True else check other options
    # Time Complexity: O(9^(N^2) for every cell on board we check for 9  possibilities
    # Space Complexity: O(N) Auxiliary Space
    
    # Check if possible to place digit at row and column
    def check_possible(row,col,digit):
        for i in range(9):

	    # Check row
            if matrix[i][col] == digit:
                return False
	    
	    # Check column
            if matrix[row][i] == digit:
                return False
	    
	    # Check sub-matrix
            if matrix[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] == digit:
                return False
        
	# If possible and not returned already, return True
	return True
    
    # BackTrack
    def backtrack():
        # 1. Loop over matrix for every to be digit added
        for i in range(9):
            for j in range(9):
                # 2. Check for unfilled spaces 
                if matrix[i][j] == 0:
                    # 3. If not filled, check possibilities of numbers to fill
                    for digit in range(1,10):
                         if check_possible(i,j,digit):
                            # 3. Assign Digit
                            matrix[i][j] = digit
                            if backtrack():
                                return True
                            else:
                            # 4. If digit didn't work in backtrack, unassign
                                matrix[i][j] = 0         
                    return False       
        return True
    
    # Fill empty cells with backtracking one by one as per traversal of matrix  
    if backtrack():
        return True
