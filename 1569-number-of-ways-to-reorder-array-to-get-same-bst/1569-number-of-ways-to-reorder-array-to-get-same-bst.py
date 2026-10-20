class Solution:
    def numOfWays(self, nums: list[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        pos = [0] * n
        for i, x in enumerate(nums):
            pos[x - 1] = i

        left = [-1] * n
        right = [-1] * n
        stack = []

        for i in range(n):
            last = -1

            while stack and pos[stack[-1]] > pos[i]:
                last = stack.pop()

            if stack:
                right[stack[-1]] = i

            if last != -1:
                left[i] = last

            stack.append(i)

        root = stack[0]

        fact = [1] * (n + 1)
        invfact = [1] * (n + 1)

        for i in range(1, n + 1):
            fact[i] = fact[i - 1] * i % MOD

        invfact[n] = pow(fact[n], MOD - 2, MOD)

        for i in range(n, 0, -1):
            invfact[i - 1] = invfact[i] * i % MOD

        def comb(a, b):
            return fact[a] * invfact[b] % MOD * invfact[a - b] % MOD

        order = []
        stack = [root]

        while stack:
            u = stack.pop()
            order.append(u)

            if left[u] != -1:
                stack.append(left[u])

            if right[u] != -1:
                stack.append(right[u])

        size = [1] * n
        ways = [1] * n

        for u in reversed(order):
            l, r = left[u], right[u]
            ls = size[l] if l != -1 else 0
            rs = size[r] if r != -1 else 0

            size[u] = ls + rs + 1
            ways[u] = comb(ls + rs, ls)

            if l != -1:
                ways[u] = ways[u] * ways[l] % MOD

            if r != -1:
                ways[u] = ways[u] * ways[r] % MOD

        return (ways[root] - 1) % MOD