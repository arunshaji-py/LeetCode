# Walls and Gates - LeetCode 28

## Pattern 
***Graph -> Multi-Source BFS***
---
# Problem Statement 

You are given a m X n grid called 'rooms'.

Each cell contains one of the following values:
- -1 = walls
- 0 = gate
- `2147483647 (INF) = empty room.

# The Task
Your task is to fill every empty room (INF) with the ***distance*** from the nearest gate(0).


### Rules

- You can move only:
  - Up
  - Down
  - Left
  - Right
- You cannot move through walls.
- If a room cannot reach any gate, it should remain `INF`.
- Modify the grid **in-place**.

# Key idea 

Instead of finding the nearest gate for every empty room, we start BFS from all gates simultaneously. ( This is why we use multi-source BFS)

When we say "simultaneously", we don't literally mean the CPU is running multiple BFS algorithms in parallel.

We mean that the algorithm behaves as if every gate starts spreading at the same time.

Let's see why.
Suppose we have this grid
INF   0   INF

INF  INF  INF

0    INF  INF

There are two gates.

Coordinates:
Gate 1 → (0,1)

Gate 2 → (2,0)

Step 1: Initial Queue
During the first traversal, we add all gates to the queue.
queue = [    (0,1),    (2,0)]


Notice something?

We haven't started BFS yet.

Both gates are already waiting in the queue.
Step 2: Start BFS
The queue looks like this:
Front

(0,1)

(2,0)

Rear

We process (0,1) first.

It updates its neighbours.
Queue becomes

(2,0)

(0,0)

(0,2)

(1,1)

Now we process (2,0).

It also updates its neighbours.

Queue becomes
(0,0)

(0,2)

(1,1)

(1,0)

(2,1)

What happened?
Although the CPU processed one gate first and the other gate second, both gates belonged to the same BFS level (distance 0).

# Why BFS?

BFS explores the graph **level by level**.

Each BFS level represents **one additional step away from the nearest gate**.

Because of this property, the first time we visit an empty room is guaranteed to be its shortest distance from a gate.

DFS cannot guarantee the shortest distance.

---


# Algorithm

## Step 1

Check whether the grid is empty.

```python
if not rooms:
    return
```

---

## Step 2

Get the number of rows and columns.

```python
rows = len(rooms)
cols = len(rooms[0])
```

---

## Step 3

Create an empty queue.

```python
queue = deque()
```

The queue stores the coordinates of all gates.

---

## Step 4

Traverse the entire grid.

Whenever a gate (`0`) is found,

add its coordinates to the queue.

```python
if rooms[r][c] == 0:
    queue.append((r, c))
```

---

## Step 5

Create the four directions.

```python
directions = [
    (-1, 0),  # Up
    (1, 0),   # Down
    (0, -1),  # Left
    (0, 1)    # Right
]
```

---

## Step 6

Perform Multi-Source BFS.

```python
while queue:
```

Remove one cell.

```python
r, c = queue.popleft()
```

Visit its four neighbouring cells.

---

## Step 7

For every neighbouring cell,

check

- Is it inside the grid?
- Is it an empty room (`INF`)?

```python
0 <= new_row < rows
0 <= new_col < cols
rooms[new_row][new_col] == 2147483647
```

---

## Step 8

Update the neighbouring room.

```python
rooms[new_row][new_col] = rooms[r][c] + 1
```

Why?

The current room already stores the shortest distance to the nearest gate.

Therefore, the neighbouring room must be **one step farther away**.

---

## Step 9

Add the newly updated room to the queue.

```python
queue.append((new_row, new_col))
```

Continue until the queue becomes empty.

---


