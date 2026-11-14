class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n = len(nums)
        ans = float('inf')

        for size in range(l, r + 1):
            curr = sum(nums[:size])

            if 0 < curr < ans:
                ans = curr

            for i in range(size, n):
                curr += nums[i] - nums[i - size]

                if 0 < curr < ans:
                    ans = curr

                if ans == 1:
                    return 1

        return ans if ans != float('inf') else -1