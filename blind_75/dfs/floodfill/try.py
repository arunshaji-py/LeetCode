class Solution:
    def floodFill(self,image, sr, sc, color):
        if not image:
            return image
        
        #get the rows and cols
        rows = len(image)
        cols = len(image[0])

        original_color = image[sr][sc]

        # if the cells are already the same color to which it must be changed.
        if image[sr][sc] == color:
            return 
        
        # now define the dfs function
        def dfs(r, c):
            #check whether the cell is outside the grid or the color of cell is different
            if (
                r < 0 or r >= rows or
                c < 0 or c >= cols or
                image[r][c] != original_color
            ):
                return
            
            #if the checks are passed, assign the color to the cell before going to the neibours
            image[r][c] = color

            #using recursion call visit all the neibours
            dfs(r + 1, c) #down
            dfs(r - 1, c) #up
            dfs(r, c + 1) #right
            dfs(r, c - 1) #left
        
        dfs(sr,sc)
        return image