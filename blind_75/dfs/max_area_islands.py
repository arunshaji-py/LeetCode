#finding the island with the max area

class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:

        #if the grid is empty 
        if not grid:
            return 0
        
        #store the visited cell, we use set() for visited because of O(1) lookup and addition (hashable)
        visited = set()
        
        #get the row and column count
        row = len(grid)
        col = len(grid[0])

        #define the four movement directions as list of tuples, we use tuples because they are immutable and represent 
        # the change in (row, column).
        directions = [
            (-1,0), #up
            (1,0), #down
            (0,-1), #left
            (0,1) #right
        ]

        #now define the dfs function 
        def dfs(r,c):


            #add the current element to the visited set()
            visited.add((r,c))
            
            #add the area by one 
            area = 1

            for dr,dc in directions:

                #declare the new_rol and new_col
                new_row = dr + r
                new_col = dc + c

                if (
                    0 <= new_row < row
                and 0 <= new_col < col
                and grid[new_row][new_col] == 1
                and (new_row,new_col) not in visited
                ):
                    #add the area of the neibours
                    area += dfs(new_row, new_col)

            return area

            

        max_area = 0
        #define the nested loop to traverse each coordinates or elements in the grid.
        for r in range(row):
            for c in range(col):
                if(
                    grid[r][c] == 1
                    and (r,c) not in visited

                ):
                    area = dfs(r,c)
                    max_area = max(max_area,area)
        return max_area


        
