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

### Important Concept **level order BFS** 

Every level of BFS represents one minute. We deliberately process the queue level by level. 

The technique is to use the for loop wisely.

The trick: Process one BFS level at a time
Before processing a minute, we record:
level_size = len(queue)


Suppose:
queue = deque([    (0,0),    (2,2)])


Then:
level_size = 2


Now we process exactly 2 oranges:
for _ in range(level_size):    r, c = queue.popleft()    # Rot neighbours    # Add newly rotten oranges to queue


Any newly rotten oranges are added to the back of the queue, but they are not processed yet because this for loop only runs level_size times.

Once those 2 oranges have finished spreading:
minutes += 1


Now the queue contains only the oranges that became rotten during the previous minute.

Those will spread during the next minute.

### Use of Deque as Queue, append() and popleft()

***append()***
We use append() to add cells to the queue. append() will add new items to the right.

***popleft()***
we use popleft() to take out the first added items. 

So, the rotten oranges first added will get processed 1st and then the oranges that are added later gets processed. 

So it is a Queue or it will be a stack. 



### Pattern to remember
If a problem says something spreads simultaneously every minute, every second, every step, or every level, your first thought should be "Can I solve this with level-order BFS?"

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