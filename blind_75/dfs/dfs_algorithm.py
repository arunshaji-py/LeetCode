from collections import deque

def dfs( self, grid: list[list[str]]) -> int:

    if not grid:
        return 0
    
    rows = len(grid)
    cols = len(grid[0])

    
    visited = set()

    #direction which is a list of tuples
    direction = [
        (-1,0), #up
        (1,0), #down
        (0,-1), #left
        (0,1) #right

    ]

    def dfs(r,c):
        visited.add(r,c)

        #define the outer loop to reach each element 
        for dr, dc in direction:
            
            new_row = r + dr
            new_col = c + dc

            if (
                0 <= new_row < rows and 
                0 <= new_col < cols and
                grid[new_row][new_col] == "1"
                and (new_row,new_row) not in visited
            ):
                #do the recursive call 
                dfs(new_row,new_col)

    islands = 0

    for r in range(rows):
        for c in range(cols):
            if (
                grid[r][c] == "1"
                and (r,c) not in visited
            ):
                islands += 1
                dfs(r,c)
    return islands


