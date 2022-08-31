import numpy as np

def ratInAMaze(maze, n):
    visited = [[0 for i in range(n)] for j in range(n)]
    
    def recur_explore(i, j):  
        visited[i][j] = 1
        
        if i == n-1 and j == n-1: 
            # Base Case
            # Print every path as a flattened visited array separated by spaces
            flatten_list = sum(visited, [])
            print(' '.join(str(e) for e in flatten_list))
            return
        
        if i+1 < n and not visited[i+1][j] and maze[i+1][j] == 1:
            # Right
            recur_explore(i+1,j)
            visited[i+1][j] = 0
        
        if j+1 < n and not visited[i][j+1] and maze[i][j+1] == 1:
            # Bottom
            recur_explore(i,j+1)
            visited[i][j+1] = 0
        
        if i-1 > -1 and not visited[i-1][j] and maze[i-1][j] == 1:
            # Left
            recur_explore(i-1,j)
            visited[i-1][j] = 0
        
        if j-1 > -1 and not visited[i][j-1] and maze[i][j-1] == 1:
            # Up
            recur_explore(i,j-1)
            visited[i][j-1] = 0
    
    if maze[0][0] == 0 or maze[n-1][n-1] == 0:
        return []
    recur_explore(0, 0)    
      
    
# Main.
n = int(input())
maze = n*[0]

for i in range(0 , n):
    maze[i]=input().split()
    maze[i]=[int(j) for j in maze[i]]
    
ratInAMaze(maze , n) 
