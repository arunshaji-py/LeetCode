from collections import deque
class Solution:
    def wallsAndGates(self, rooms: list[list[int]]) -> None:
        # process empty rooms
        if not rooms:
            return 
        
        # process the rows and calls.
        rows = len(rooms)
        cols = len(rooms[0])

        # declare a queue
        queue = deque()

        # during the first traversal take all the gates into the queue

        for r in range(rows):
            for c in range(cols):
                if rooms[r][c] == 0:
                    queue.append((r, c))
        
        # Now define the directions for neibour traversal
        directions = [
            (-1, 0), #up
            (1, 0), #down
            (0, -1), #left
            (0, 1) #right

        ]

        # using a while loop continue the BFS
        while queue:

            r, c = queue.popleft()

            # visit all four neighbouring cells
            for dr, dc in directions:

                new_row = dr + r
                new_col = dc + c

                # check whether the neighbouring cells is inside the rooms
                # and is an empty room (INF)
                if (
                    0 <= new_row < rows and
                    0 <= new_col < cols and
                    rooms[new_row][new_col] == 2147483647
                ):
                    # store the shortest distance to the nearest gate at that cell
                    rooms[new_row][new_col] = rooms[r][c] + 1

                    # add the newly updated room to the queue
                    queue.append((new_row, new_col))


        
