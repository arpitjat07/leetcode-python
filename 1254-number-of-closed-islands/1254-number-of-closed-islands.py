class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def dfs(r, c):
            if r < 0 or r >= m or c < 0 or c >= n:
                return 0
            if grid[r][c] == 1:
                return 1

            grid[r][c] = 1

            a = dfs(r - 1, c)
            b = dfs(r + 1, c)
            d = dfs(r, c - 1)
            e = dfs(r, c + 1)

            return a & b & d & e

        ans = 0

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    ans += dfs(r, c)

        return ans