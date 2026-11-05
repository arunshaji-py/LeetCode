#leetcode 733 - Flood Fill

## Problem
The problem is to change the color of cells which are same as the starting cell color. 
Starting at (sr,sc), change that cell and all four-directionally connected cells with the same color to the new color. 

## Concept 
Grid as a graph. Each cell is a node. Up,down,left, and the right are its possible niebours,  Diagonal cells don't connect. 

## DFS idea
Start at the given cell and 'recursively' explore its connected neighbours that match the original color.

## Stopping conditions
Return if a cell is outside the grid or its color differs from the original color.

## Visited tracking.
Change a matching cell color 'before' visiting the neibours.It no longer matches the orginal color again, so recoloring the same cell can be prevented.

## Neibour calls
Recurse to (r + 1, c), (r -1, c), ( r, C + 1), ( r, c - 1).

## Complexity 
For an m X n  imagem time is O(mn) in the worse case.
Time is O(mn) for recursive stack call. 
