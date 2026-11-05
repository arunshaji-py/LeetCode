class Solution:
    def floodFill(self, image, sr, sc, color):
        #return 0 if empty grid
        if not image:
            return 0
        
        #read the rows and cols
        rows = len(image)
        cols = len(image[0])

        original_color = image[sr][sc]

        #if the color is already the requested color, return the image
        if original_color == color:
            return image
        
        #now define the dfs
        def dfs(r, c):
            #check whether r, c is outside the grid or has a different colour than the starting cell color
            if (
                r < 0 or r >= rows or
                c < 0 or c >= cols or
                image[r][c] != original_color
            ):
                return 
            
            #if the check passes, change the color of that cell to the new desired color.
            image[r][c] = color

            #now, recursively do the same for the neibouring cells
            dfs(r + 1, c) #down
            dfs(r - 1, c) #up
            dfs(r, c + 1) #right
            dfs(r, c - 1) #left
        
        dfs(sr, sc)
        return image
