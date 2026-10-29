class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        LOG = n.bit_length()
        parent = [[0] * n for _ in range(LOG)]
        depth = [0] * n
        tin = [0] * n
        tout = [0] * n
        timer = 0

        stack = [(0, -1, 0)]
        while stack:
            u, p, state = stack.pop()

            if state == 0:
                parent[0][u] = u if p == -1 else p
                tin[u] = timer
                timer += 1
                stack.append((u, p, 1))

                for v in graph[u]:
                    if v != p:
                        depth[v] = depth[u] + 1
                        stack.append((v, u, 0))
            else:
                tout[u] = timer - 1

        for j in range(1, LOG):
            prev = parent[j - 1]
            curr = parent[j]
            for u in range(n):
                curr[u] = prev[prev[u]]

        bit = [0] * (n + 2)

        def update(i, value):
            i += 1
            while i <= n:
                bit[i] ^= value
                i += i & -i

        def prefix(i):
            result = 0
            i += 1
            while i > 0:
                result ^= bit[i]
                i -= i & -i
            return result

        def range_update(l, r, value):
            update(l, value)
            if r + 1 < n:
                update(r + 1, value)

        def get_mask(u):
            return prefix(tin[u])

        for u, ch in enumerate(s):
            range_update(tin[u], tout[u], 1 << (ord(ch) - 97))

        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u

            diff = depth[u] - depth[v]
            for j in range(LOG):
                if diff >> j & 1:
                    u = parent[j][u]

            if u == v:
                return u

            for j in range(LOG - 1, -1, -1):
                if parent[j][u] != parent[j][v]:
                    u = parent[j][u]
                    v = parent[j][v]

            return parent[0][u]

        chars = list(s)
        ans = []

        for q in queries:
            parts = q.split()

            if parts[0] == "update":
                u = int(parts[1])
                c = parts[2]
                if chars[u] != c:
                    mask = (1 << (ord(chars[u]) - 97)) ^ (1 << (ord(c) - 97))
                    range_update(tin[u], tout[u], mask)
                    chars[u] = c
            else:
                u, v = int(parts[1]), int(parts[2])
                w = lca(u, v)
                mask = get_mask(u) ^ get_mask(v) ^ (1 << (ord(chars[w]) - 97))
                ans.append(mask & (mask - 1) == 0)

        return ans