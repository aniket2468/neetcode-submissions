class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        fresh_count = 0
        # Directions for moving up, down, left, or right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # Initialize the queue with all treasure cells
        queue = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:  # Treasure chest
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    fresh_count += 1
        
        if fresh_count == 0:
            return 0
        
        minutes = 0
        # Perform BFS
        while queue:
            for _ in range(len(queue)):
                x, y = queue.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    # If the neighbor is a fresh orange
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                        grid[nx][ny] = 2  # Rot the orange
                        queue.append((nx, ny))
                        fresh_count -= 1
            minutes += 1

        # If there are still fresh oranges, return -1
        return minutes - 1 if fresh_count == 0 else -1