def solution():
    m, n = map(int, input().split())

    matrix_grid = []
    for _ in range(m):
        matrix_grid.append(input().split())

    island_counter = 0

    def dfs(i, j):
        # boundary + water check
        if i < 0 or i >= m or j < 0 or j >= n or matrix_grid[i][j] == '0':
            return

        # mark visited
        matrix_grid[i][j] = '0'

        # explore all 4 directions
        dfs(i + 1, j)
        dfs(i - 1, j)
        dfs(i, j + 1)
        dfs(i, j - 1)

    for i in range(m):
        for j in range(n):
            if matrix_grid[i][j] == '1':
                island_counter += 1
                dfs(i, j)

    return island_counter


print(solution())