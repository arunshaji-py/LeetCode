from collections import deque


def num_islands(grid):
    """
    Count the number of islands in the given grid using BFS.
    """

    # Handle empty grid
    if not grid:
        return 0

    # Grid dimensions
    rows = len(grid)
    cols = len(grid[0])

    # Variables
    islands = 0
    visited = set()

    # Breadth-First Search
    def bfs(r, c):
        queue = deque()

        # Add the starting cell
        queue.append((r, c))
        visited.add((r, c))

        # Four possible directions
        directions = [
            (1, 0),     # Down
            (-1, 0),    # Up
            (0, 1),     # Right
            (0, -1)     # Left
        ]

        while queue:
            row, col = queue.popleft()

            # Visit all four neighbours
            for dr, dc in directions:
                new_row = row + dr
                new_col = col + dc

                # Check whether neighbour is valid
                if (
                    0 <= new_row < rows
                    and 0 <= new_col < cols
                    and grid[new_row][new_col] == "1"
                    and (new_row, new_col) not in visited
                ):
                    visited.add((new_row, new_col))
                    queue.append((new_row, new_col))

    # Scan every cell in the grid
    for r in range(rows):
        for c in range(cols):

            # Found a new island
            if grid[r][c] == "1" and (r, c) not in visited:
                islands += 1
                bfs(r, c)

    return islands


def read_grid_from_user():
    """
    Read a valid grid from the user.
    """

    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))

    grid = []

    print("\nEnter each row using only 0 and 1.")
    print(f"Each row must contain exactly {cols} characters.\n")

    for i in range(rows):

        while True:

            row = input(f"Enter row {i + 1}: ").strip()

            # Check row length
            if len(row) != cols:
                print(f"Please enter exactly {cols} characters.")
                continue

            # Check characters
            if any(ch not in ("0", "1") for ch in row):
                print("Only 0 and 1 are allowed.")
                continue

            # Save the row
            grid.append(list(row))
            break

    return grid


def print_grid(grid):
    """
    Display the grid.
    """

    print("\nYour grid:")

    for row in grid:
        print(" ".join(row))


def main():

    grid = read_grid_from_user()

    print_grid(grid)

    islands = num_islands(grid)

    print(f"\nNumber of islands: {islands}")


if __name__ == "__main__":
    main()