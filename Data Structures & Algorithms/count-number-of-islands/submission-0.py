class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        islands = 0

        def dfs(r, c):
            # Check out of bounds + if water
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == "0":
                return

            grid[r][c] = "0" # Mark island as seen

            dfs(r + 1, c) # Move down
            dfs(r - 1, c) # Move up
            dfs(r, c + 1) # Move right
            dfs(r, c - 1) # Move left

        # Iterate through grid till we find island. If found do DSF for rest of the island
        for r in range(rows):
            for c in range(cols):

                if grid[r][c] == "1":
                    islands += 1
                    dfs(r,c)

        return islands
