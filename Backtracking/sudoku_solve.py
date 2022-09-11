def isItSudoku(matrix):
    
    # Approach: Traverse over colors to check if possible, if yes propagate True else check other options
    # Time Complexity: O(N^M) for n nodes we check m possibilities
    # Space Complexity: O(N) for color array + O(N) Auxiliary Space
    
    # Check if possible to place digit at row and column
    def check_possible(row,col,digit):
        for i in range(9):
            if matrix[i][col] == digit:
                return False

            if matrix[row][i] == digit:
                return False

            if matrix[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] == digit:
                return False
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
    
    # Colors nodes with backtracking one by one (0-N and not as per adj_list) 
    if backtrack():
        return True
