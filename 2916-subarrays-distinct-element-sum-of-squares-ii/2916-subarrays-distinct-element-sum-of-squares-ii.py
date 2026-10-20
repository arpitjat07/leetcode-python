class Solution:
    def sumCounts(self, nums: list[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        size = 4 * n
        sums = [0] * size
        sq = [0] * size
        lazy = [0] * size

        def apply(node, l, r, v):
            length = r - l + 1
            sq[node] = (sq[node] + 2 * v * sums[node] + length * v * v) % MOD
            sums[node] = (sums[node] + length * v) % MOD
            lazy[node] += v

        def push(node, l, r):
            if lazy[node]:
                mid = (l + r) // 2
                apply(node * 2, l, mid, lazy[node])
                apply(node * 2 + 1, mid + 1, r, lazy[node])
                lazy[node] = 0

        def update(node, l, r, ql, qr):
            if ql <= l and r <= qr:
                apply(node, l, r, 1)
                return
            push(node, l, r)
            mid = (l + r) // 2
            if ql <= mid:
                update(node * 2, l, mid, ql, qr)
            if qr > mid:
                update(node * 2 + 1, mid + 1, r, ql, qr)
            sums[node] = (sums[node * 2] + sums[node * 2 + 1]) % MOD
            sq[node] = (sq[node * 2] + sq[node * 2 + 1]) % MOD

        last = {}
        ans = 0

        for i, x in enumerate(nums):
            prev = last.get(x, -1)
            update(1, 0, n - 1, prev + 1, i)
            ans = (ans + sq[1]) % MOD
            last[x] = i

        return ans