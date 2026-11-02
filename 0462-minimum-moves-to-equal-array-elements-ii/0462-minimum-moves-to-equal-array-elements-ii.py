import random

class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        n = len(nums)
        target = n // 2
        left, right = 0, n - 1

        while left <= right:
            pivot = nums[random.randint(left, right)]
            i, j, k = left, left, right

            while j <= k:
                if nums[j] < pivot:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
                    j += 1
                elif nums[j] > pivot:
                    nums[j], nums[k] = nums[k], nums[j]
                    k -= 1
                else:
                    j += 1

            if target < i:
                right = i - 1
            elif target > k:
                left = k + 1
            else:
                median = nums[target]
                break

        return sum(abs(x - median) for x in nums)