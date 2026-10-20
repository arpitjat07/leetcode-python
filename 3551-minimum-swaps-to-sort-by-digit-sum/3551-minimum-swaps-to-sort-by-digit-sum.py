class Solution:
    def minSwaps(self, nums: list[int]) -> int:
        def digit_sum(x):
            return sum(map(int, str(x)))

        n = len(nums)
        target = sorted(nums, key=lambda x: (digit_sum(x), x))
        pos = {x: i for i, x in enumerate(target)}
        visited = [False] * n
        swaps = 0

        for i in range(n):
            if visited[i]:
                continue

            j = i
            cycle = 0

            while not visited[j]:
                visited[j] = True
                j = pos[nums[j]]
                cycle += 1

            swaps += cycle - 1

        return swaps