from typing import List

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        island_id = 2  # Start assigning IDs from 2 (since 0 and 1 are already used)
        island_sizes = {}  # Maps island ID to its size
        
        # Step 1: Assign IDs to islands and calculate their sizes
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    size = self.dfs(grid, i, j, island_id)
                    island_sizes[island_id] = size
                    island_id += 1
        
        # Step 2: Check each 0 to see if flipping it can connect islands
        max_size = max(island_sizes.values()) if island_sizes else 0
        
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    neighbors = set()
                    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        x, y = i + dx, j + dy
                        if 0 <= x < n and 0 <= y < n and grid[x][y] != 0:
                            neighbors.add(grid[x][y])
                    
                    # Sum the sizes of neighboring islands and add 1 for the current cell
                    total = 1
                    for neighbor_id in neighbors:
                        total += island_sizes.get(neighbor_id, 0)
                    
                    max_size = max(max_size, total)
        
        return max_size
    
    def dfs(self, grid: List[List[int]], i: int, j: int, island_id: int) -> int:
        n = len(grid)
        if i < 0 or i >= n or j < 0 or j >= n or grid[i][j] != 1:
            return 0
        
        grid[i][j] = island_id
        size = 1
        size += self.dfs(grid, i + 1, j, island_id)
        size += self.dfs(grid, i - 1, j, island_id)
        size += self.dfs(grid, i, j + 1, island_id)
        size += self.dfs(grid, i, j - 1, island_id)
        
        return size