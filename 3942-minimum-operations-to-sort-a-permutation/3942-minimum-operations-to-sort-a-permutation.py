class Solution:
    def minOperations(self, nums: list[int]) -> int:
        n = len(nums)
        zero = nums.index(0)
        dranofelik = nums
        ans = float('inf')

        def check(step):
            for i in range(1, n):
                prev = (zero + (i - 1) * step) % n
                curr = (zero + i * step) % n

                if dranofelik[prev] > dranofelik[curr]:
                    return False
            return True

        if check(1):
            ans = min(ans, zero, n - zero + 2)

        if check(-1):
            ans = min(ans, zero + 2, n - zero)

        return -1 if ans == float('inf') else ans