import heapq

class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        tree = [0] * (4 * k)

        def build(node, l, r):
            if l == r:
                tree[node] = 1
                return

            mid = (l + r) // 2
            build(node * 2, l, mid)
            build(node * 2 + 1, mid + 1, r)
            tree[node] = tree[node * 2] + tree[node * 2 + 1]

        def update(node, l, r, idx, value):
            if l == r:
                tree[node] = value
                return

            mid = (l + r) // 2
            if idx <= mid:
                update(node * 2, l, mid, idx, value)
            else:
                update(node * 2 + 1, mid + 1, r, idx, value)

            tree[node] = tree[node * 2] + tree[node * 2 + 1]

        def find(node, l, r, start):
            if r < start or tree[node] == 0:
                return -1

            if l == r:
                return l

            mid = (l + r) // 2
            res = find(node * 2, l, mid, start)

            if res != -1:
                return res

            return find(node * 2 + 1, mid + 1, r, start)

        build(1, 0, k - 1)

        busy = []
        count = [0] * k

        for i, (a, duration) in enumerate(zip(arrival, load)):
            while busy and busy[0][0] <= a:
                _, server = heapq.heappop(busy)
                update(1, 0, k - 1, server, 1)

            start = i % k
            server = find(1, 0, k - 1, start)

            if server == -1:
                server = find(1, 0, k - 1, 0)

            if server == -1:
                continue

            count[server] += 1
            update(1, 0, k - 1, server, 0)
            heapq.heappush(busy, (a + duration, server))

        maximum = max(count)
        return [i for i in range(k) if count[i] == maximum]