







directions = [
        (1,0), #down
        (-1,0), #up
        (0,1), #right
        (0,-1) #left
    ]
visited = set()
#define the dfs brain
def dfs (r,c):
    area = 1
    visited.add((r,c))


    for dr, dc in directions:
        new_row = dr + r
        new_col = dc + c
        if(
            0 <= new_row < rows 
            and 0<= new_col < cols
            and grid[new_row][new_col] == "1"
            and (new_row, new_col) not in visited

        ):
           area += dfs(new_row, new_col)
    return area

max_area = 0
for r in range(rows):
    for c in range(cols):
        if( 
            grid[r][c] == "1" 
        and (r,c) not in visited
        ):
            area = dfs(r,c)
            max_area = max(max_area,area)