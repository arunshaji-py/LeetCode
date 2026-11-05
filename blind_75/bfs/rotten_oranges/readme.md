# leetcode 994 - Rotting Oranges
## Difficulty : Medium
## Pattern : Graph Traversal
## Algorithm : Breadth First Search (BFS)
## Data Structure : Queue (deque (python) )

### Problem Statement

You are given a 2D grid where:
- 0 represents an empty cell.
- 1 represents a fresh orange.
- 2 represents a rotten orange.

Every minute, every rotten orange turns all of its adjacent fresh oranges rotten.

Ajcacent means:
- up
- down
- left 
- right

! Diagonals are not accepted.

### Objectives

- Return the 'minimum number of minutes' required until no fresh orange is left.
- If it is impossible for every fresh orange to become rotten, return -1. 

# Why is this a Graph Problem?

A 2D grid can be viewed as a graph.

Each cell is a node.

Each node is connected to its four neighbouring cells.

        Up
         |
Left — Cell — Right
         |
       Down

The infection spreads from one node to another through these connections.

---

# Why BFS?

Unlike DFS, this problem asks us to calculate the **minimum time** needed for the infection to spread.

BFS explores nodes **level by level**.

Each level of BFS represents **one minute**.

Therefore BFS naturally models the spread of infection over time.

---

# New Concept Learned

## Multi-Source BFS

This is the first problem where BFS does **not** start from a single node.

Instead,

**every rotten orange is a starting node.**

Before BFS begins,

we place the coordinates of **all rotten oranges** into the queue.

The infection then spreads simultaneously from all of them.

This technique is called **Multi-Source BFS**.

---