from collections import deque



def read_grid_from_user():
    #read the rows and cols from the user
    rows = int(input("please enter the number of rows.  "))
    cols = int(input("please enter the number of cols. "))

    #now read the each row elements into the grid
    #declare a grid
    grid =[]

    print("please enter each row elements using 0 and 1 only. ")
    print(f"Each row should contain {cols} elements. ")

    #using a for and while loop combo read the valid inputs from the user
    for i in range(rows):
        while True:
            row = input(f"please input row {i + 1}, ")

            #check if the entered row is valid with number of cols 
            if len(row) != cols:
                print(f"please enter exactly {cols} elements into the row. ")
                continue

            #check if the entered row elements only contain 0 and 1
            if any(ch not in ("0","1") for ch in row ):
                print("elemets should only be 0 and 1 ")
                continue
            
            #if both the checks are valid, save that row to the grid
            grid.append(list(row))
            break
    return grid
    
#def the function to print the grid 
def print_grid(grid):
    print("\n your grid")

    for row in grid:
        print(" ".join(row))


#define the brain of the solution
def number_of_islands(grid):
    #handle an empty grid
    if not grid:
        return 0
    
    #now using breadth first search (bfs) lets find the number of islands in the problem.

    #grid diamensions
    rows = len(grid)
    cols = len(grid[0])

    #variables
    islands = 0
    visited = set()

    #scan for every cell in the grid
    for r in range(rows):
        for c in range(cols):
            #enter the element into the islands and visited queue if its a 1
            if grid[r][c] == "1" and (r,c) not in visited:
                islands += 1
                bfs(r,c)
    
    def bfs(r,c):
        queue = deque()
        
        #add the starting cell into the visited and queue
        queue.append((r,c))
        visited.add((r,c))

        #now define a list with the possible for directions
        directions = [
            (1,0),  #dowm
            (-1,0), #up
            (0,1),  #right
            (0,-1)  #left
        ]

        #check for islands untill the queue is empty
        while queue:
            row, col = queue.popleft()

            #visit all the neibours of the coordinate in the queue
            for dr, dc in directions:
                new_row = row + dr
                new_col = col + dc

                #check for one
                if (
                    0 <= new_row < rows
                    and 0 <= new_col < cols
                    and grid[new_row][new_col] == "1"
                    and (new_row,new_col) not in visited
                ):
                    visited.add((new_row,new_col))
                    queue.append((new_row,new_col))
    return islands


def main():
    grid = read_grid_from_user()

    print_grid(grid)

    islands = number_of_islands(grid)

    print(f"number of island are {islands} ")



if __name__ == "__main__":
    main()
