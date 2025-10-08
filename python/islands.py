def numIslands(grid):
    if not grid:
        return 0

    num_rows = len(grid)
    num_cols = len(grid[0])
    count = 0

    def dfs(row, col):
        if row < 0 or row >= num_rows or col < 0 or col >= num_cols or grid[row][col] == '0':
            return
        
        grid[row][col] = '0'  # Mark as visited
        dfs(row + 1, col)     # Explore down
        dfs(row - 1, col)     # Explore up
        dfs(row, col + 1)     # Explore right
        dfs(row, col - 1)     # Explore left
        

    for i in range(num_rows):
        for j in range(num_cols):
            if grid[i][j] == '1':
                count += 1
                dfs(i, j)

    return count
