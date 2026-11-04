class Solution:
    def minOperations(self, nums: list[int], x: int, k: int) -> int:
        n = len(nums)
        values = sorted(set(nums))
        m = len(values)
        pos = {v: i + 1 for i, v in enumerate(values)}

        bit_count = [0] * (m + 1)
        bit_sum = [0] * (m + 1)

        def update(v, delta):
            i = pos[v]
            while i <= m:
                bit_count[i] += delta
                bit_sum[i] += delta * v
                i += i & -i

        def kth(rank):
            idx = 0
            step = 1 << (m.bit_length() - 1)

            while step:
                nxt = idx + step
                if nxt <= m and bit_count[nxt] < rank:
                    rank -= bit_count[nxt]
                    idx = nxt
                step >>= 1

            return idx + 1

        def prefix(i):
            count = total = 0
            while i:
                count += bit_count[i]
                total += bit_sum[i]
                i -= i & -i
            return count, total

        costs = []
        window_sum = 0

        for i, v in enumerate(nums):
            update(v, 1)
            window_sum += v

            if i >= x:
                old = nums[i - x]
                update(old, -1)
                window_sum -= old

            if i >= x - 1:
                p = kth((x + 1) // 2)
                median = values[p - 1]
                count, left_sum = prefix(p)

                cost = (
                    median * count - left_sum
                    + window_sum - left_sum
                    - median * (x - count)
                )

                costs.append(cost)

        slack = n - k * x
        INF = float('inf')
        prev = [0] * (slack + 1)

        for t in range(1, k + 1):
            curr = [INF] * (slack + 1)
            base = (t - 1) * x

            for j in range(slack + 1):
                pick = prev[j] + costs[base + j]
                skip = curr[j - 1] if j else INF
                curr[j] = min(pick, skip)

            prev = curr

        return prev[slack]