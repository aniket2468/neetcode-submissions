class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        m, n = len(grid), len(grid[0])
        INF = 2147483647

        # Directions for moving up, down, left, or right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # Initialize the queue with all treasure cells
        queue = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:  # Treasure chest
                    queue.append((i, j))

        # Perform BFS
        while queue:
            x, y = queue.popleft()

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                # If the neighbor is a land cell (INF) and hasn't been visited
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == INF:
                    grid[nx][ny] = grid[x][y] + 1
                    queue.append((nx, ny))