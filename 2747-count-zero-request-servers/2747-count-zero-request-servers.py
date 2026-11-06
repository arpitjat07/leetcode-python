class Solution:
    def countServers(self, n: int, logs: list[list[int]], x: int, queries: list[int]) -> list[int]:
        logs.sort(key=lambda a: a[1])
        q = sorted((t, i) for i, t in enumerate(queries))

        freq = [0] * (n + 1)
        ans = [0] * len(queries)

        left = right = active = 0
        m = len(logs)

        for t, idx in q:
            while right < m and logs[right][1] <= t:
                server = logs[right][0]
                if freq[server] == 0:
                    active += 1
                freq[server] += 1
                right += 1

            while left < right and logs[left][1] < t - x:
                server = logs[left][0]
                freq[server] -= 1
                if freq[server] == 0:
                    active -= 1
                left += 1

            ans[idx] = n - active

        return ans