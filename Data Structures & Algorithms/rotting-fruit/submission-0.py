class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        fresh = 0
        minutes = 0
        queue = deque()

        # Find all the positions of the rotten oranges
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                if grid[r][c] == 1:
                    fresh += 1

        while queue and fresh > 0:
            level_size = len(queue)

            for i in range(level_size):
                r, c = queue.popleft()

                directions = [
                    (1, 0),  # right
                    (-1, 0),  # left
                    (0, 1),  # up
                    (0, -1),  # down
                ]

                for dr, dc in directions:
                    new_r = r + dr
                    new_c = c + dc

                    if 0 <= new_r < rows and 0 <= new_c < cols and grid[new_r][new_c] == 1:
                        grid[new_r][new_c] = 2
                        fresh -= 1
                        queue.append((new_r, new_c))
            minutes += 1

        return minutes if fresh == 0 else -1
