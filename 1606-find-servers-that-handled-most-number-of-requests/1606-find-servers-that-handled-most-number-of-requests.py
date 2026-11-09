import heapq

class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        free = list(range(k))
        busy = []
        count = [0] * k

        for i, (start, duration) in enumerate(zip(arrival, load)):
            while busy and busy[0][0] <= start:
                _, server = heapq.heappop(busy)
                heapq.heappush(free, i + (server - i) % k)

            if not free:
                continue

            server = heapq.heappop(free) % k

            count[server] += 1
            heapq.heappush(busy, (start + duration, server))

        maximum = max(count)
        return [i for i, c in enumerate(count) if c == maximum]