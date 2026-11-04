import heapq

class Solution:
    def minOperations(self, nums: list[int], x: int, k: int) -> int:
        small, large = [], []
        delayed = {}

        small_size = large_size = 0
        small_sum = large_sum = 0

        def prune_small():
            while small:
                v = -small[0]
                if delayed.get(v, 0) == 0:
                    break
                heapq.heappop(small)
                delayed[v] -= 1
                if delayed[v] == 0:
                    del delayed[v]

        def prune_large():
            while large:
                v = large[0]
                if delayed.get(v, 0) == 0:
                    break
                heapq.heappop(large)
                delayed[v] -= 1
                if delayed[v] == 0:
                    del delayed[v]

        def rebalance():
            nonlocal small_size, large_size, small_sum, large_sum

            prune_small()
            prune_large()

            if small_size > large_size + 1:
                v = -heapq.heappop(small)
                small_size -= 1
                small_sum -= v
                heapq.heappush(large, v)
                large_size += 1
                large_sum += v

            elif small_size < large_size:
                v = heapq.heappop(large)
                large_size -= 1
                large_sum -= v
                heapq.heappush(small, -v)
                small_size += 1
                small_sum += v

            prune_small()
            prune_large()

        def add(v):
            nonlocal small_size, large_size, small_sum, large_sum

            prune_small()
            prune_large()

            if not small or v <= -small[0]:
                heapq.heappush(small, -v)
                small_size += 1
                small_sum += v
            else:
                heapq.heappush(large, v)
                large_size += 1
                large_sum += v

            rebalance()

        def remove(v):
            nonlocal small_size, large_size, small_sum, large_sum

            prune_small()
            prune_large()

            median = -small[0]
            delayed[v] = delayed.get(v, 0) + 1

            if v <= median:
                small_size -= 1
                small_sum -= v
                if v == median:
                    prune_small()
            else:
                large_size -= 1
                large_sum -= v
                if large and v == large[0]:
                    prune_large()

            rebalance()

        def get_cost():
            prune_small()
            prune_large()

            median = -small[0]
            return (
                median * small_size - small_sum
                + large_sum - median * large_size
            )

        n = len(nums)
        costs = []

        for v in nums[:x]:
            add(v)

        costs.append(get_cost())

        for i in range(x, n):
            remove(nums[i - x])
            add(nums[i])
            costs.append(get_cost())

        maritovexi = (nums, x, k)

        INF = float('inf')
        prev = [0] * (n + 1)

        for t in range(1, k + 1):
            curr = [INF] * (n + 1)

            for i in range(t * x, n + 1):
                curr[i] = curr[i - 1]
                start = i - x

                curr[i] = min(
                    curr[i],
                    prev[start] + costs[start]
                )

            prev = curr

        return prev[n]