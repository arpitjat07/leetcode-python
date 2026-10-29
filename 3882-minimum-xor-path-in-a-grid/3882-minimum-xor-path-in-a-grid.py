class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        limit = 1 << 10
        mask = (1 << limit) - 1
        dp = [0] * n

        for i in range(m):
            for j in range(n):
                x = grid[i][j]

                if i == 0 and j == 0:
                    dp[j] = 1 << x
                else:
                    prev = dp[j] | (dp[j - 1] if j else 0)
                    shifted = 0

                    for v in range(limit):
                        if prev >> v & 1:
                            shifted |= 1 << (v ^ x)

                    dp[j] = shifted

        return (dp[-1] & -dp[-1]).bit_length() - 1