class Solution:
    def floodFill(self, image, sr, sc, color):
        rows = len(image)
        cols = len(image[0])

        original_color = image[sr][sc]

        #if the color is already the requested color, 
        # no work is needed, return the image
        if original_color == color:
            return image
        
        #define the dfs
        def dfs(r, c):
            #stop if the cell is outside the grid and the cell 
            #different color
            if(
                r < 0 or r >= rows or
                c < 0 or c >= cols or
                image[r][c] != original_color
            ):
                return
            
            #if a cell with same color found, recolor it before
            #moving to neibouring cell. 
            image[r][c] = color

            #using recursion, visited the neibours
            dfs(r + 1, c) #down
            dfs(r - 1, c) #up 
            dfs(r, c + 1) #right
            dfs(r, c - 1) #left 
        
        dfs(sr,sc)
        return image

