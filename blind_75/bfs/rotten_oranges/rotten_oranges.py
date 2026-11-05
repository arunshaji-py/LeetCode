from collections import deque
class Solution:
    def orangesRotting(self, grid: list[list[int]] ) -> int:

        # if the grid is empty
        if not grid:
            return 0
        
        # get the rows and cols
        rows = len(grid)
        cols = len(grid[0])

        # declare a queue to store all the rotten oranges
        queue = deque()

        # declare a variable to keep track of fresh oranges
        fresh = 0

        # define the list of tuples for the four directions
        directions = [
            (-1, 0), #up
            (1, 0), #down
            (0, -1), #left
            (0, 1) #right
        ]

        # during the first traversal count the number of rotten oranges
        # and count the number of fresh oranges
        for r in range(rows):
            for c in range(cols):

                #add all the rotten oranges to the queue
                if grid[r][c] == 2:
                    queue.append((r, c))
                
                #count the number of fresh oranges
                elif grid[r][c] == 1:
                    fresh += 1
        
        # if there are not fresh oranges found after the traversal,return 0
        if fresh == 0:
            return 0
        
        # declare a minute variable to store the minutes taken.
        minutes = 0

        # now perform multi source BFS
        while queue and fresh > 0:
            
            # number of rotten oranges that will spread during 
            # current minute
            level_size = len(queue)

            # process one BFS level (one minute)
            for _ in range(level_size):
                r, c = queue.popleft()

            # visit all four neibours

                for dr, dc in directions:
                    
                    new_row = r + dr
                    new_col = c + dc

                    # check whether the neibour is inside grid and is fresh
                    if (
                        0 <= new_row < rows 
                        and 0 <= new_col < cols
                        and grid[new_row][new_col] == 1
                    ):
                        # rot the fresh orange
                        grid[new_row][new_col] = 2

                        # decrease the number of fresh orange
                        fresh -= 1

                        # add the current newly rotten orange to the rotten queue
                        queue.append((new_row, new_col))

            # increase the minute variable for this operation
            minutes += 1
        
        # after all the while loop iterations,
        # check if fresh is 0 or not 
        if fresh == 0:
            return minutes
        
        #if fresh is not 0, some isolated orange ramains
        return -1





