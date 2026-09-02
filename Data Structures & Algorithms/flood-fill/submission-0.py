class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        originalColour = image[sr][sc]

        if originalColour == color:
            return image

        rows = len(image)
        cols = len(image[0])

        def dfs(r, c):
            # Check bounds + if image matches original colour
            if (r < 0 or r >= rows or c < 0 or c >= cols or image[r][c] != originalColour):
                return
            
            image[r][c] = color

            dfs(r + 1, c) # Move down
            dfs(r - 1, c) # Move up
            dfs(r, c + 1) # Move right
            dfs(r, c - 1) # Move left
        
        dfs(sr, sc)

        return image
