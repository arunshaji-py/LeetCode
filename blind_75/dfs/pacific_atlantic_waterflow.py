class Solution:
    def paceficAtlantic(self,heights: list[list[int]]) -> list[list[int]]:
        #if the grid is empty
        if not heights:
            return []
        
        #get the rows and columns
        rows = len(heights)
        cols = len(heights[0])

        #store already visited cells from pacific and atlantic
        pacific = set()
        atlantic = set()

        #define the dfs function
        def dfs(row, col, visited, previous_height):
            #base cases
            if(
                row < 0 or row >= rows or
                col < 0 or col >= cols or
                (row, col) in visited or 
                heights[row][col] < previous_height
            ): 
                return 
            
            #mark current cell as visited 
            visited.add(row, col)

            #explore all the four directions
            dfs(row + 1, col, visited, heights[row][col])
            dfs(row - 1, col, visited, heights[row][col])
            dfs(row, col + 1, visited, heights[row][col])
            dfs(row, col - 1, visited, heights[row][col])


        #start from pacific borders
        for col in range(cols):
            dfs(0, col, pacific, heights[0][col])

        for row in range(rows):
            dfs(row, 0, pacific, heights[0][row])

        #start from atlantic borders
        for col in range(cols):
            dfs(rows - 1, col, atlantic, heights[rows-1][col])

        for row in range(rows):
            dfs( rows, cols - 1, atlantic, heights[row][cols - 1])
        
        #cells reachable from both the oceans
        result = []
        for row in range(rows):
            for col in range(cols):
                if (row, col) in pacific and (row, col ) in atlantic:
                    result.append([row, col])

        return result
        


        
        


