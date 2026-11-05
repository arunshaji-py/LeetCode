from collections import deque
class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        # return 0 if empty list
        if not grid:
            return 0
        
        # get the rows and cols
        rows = len(grid)
        cols = len(grid[0])

        # declare a deque for storing all the rotten oranges
        queue = deque()

        # decalre a variable 'fresh' for storing the fresh oranges
        fresh = 0

        # do the intial traversal to count the number of rotten and fresh oranges
        for r in range(rows):
            for c in range(cols):

                # if its a rotten orange, append to the queue
                if grid[r][c] == 2:
                    queue.append((r, c))
                # if its fresh orange, increment fresh
                elif grid[r][c] == 1:
                    fresh += 1
            
        # Check if count of fresh is 0, meaning no fresh orange in the grid, return 0 minutes
        if fresh == 0:
            return 0
        
        
        # declare the direction list of tuples
        directions = [
            (-1, 0), #up
            (1, 0), # down
            (0, -1), # left
            (0, 1) #right
        ]

        # declare a variable for minutes
        minutes = 0

        # now implement the segmented BFS using a while loop
        while queue and fresh > 0:

            # declare a variable for keeping the length of the rotten oranges queue
            level_size = len(queue)

            # now, take the first r, c from the queue using pop

            for _ in range(level_size):
                r, c = queue.popleft()

                # visit all neibours of this cell

                for dr, dc in directions:
                    
                    new_row = r + dr
                    new_col = c + dc

                    #check if the new cell is inside the grid and is fresh
                    if (
                        0 <= new_row < rows and
                        0 <= new_col < cols and
                        grid[new_row][new_col] == 1
                    ):
                        #rott the orange 
                        grid[new_row][new_col] = 2

                        #decrement the fresh by one
                        fresh -= 1

                        # add the newly rotten orange to the queue
                        queue.append((new_row, new_col))
            # increment the minute after this operation
            minutes += 1

        # after the whiile loops does it job, check for the value of fresh
        # return the minutes if fresh is 0
        if fresh == 0:
            return minutes
        
        #else if fresh is non zero,
        return -1
            





           


                 

