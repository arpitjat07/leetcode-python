from collections import deque

class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
        dq = deque()
        n = len(nums)
        j = n - 1
        cost = ans = 0

        for i in range(n - 1, -1, -1):
            num = nums[i]
            count = 1

            while dq and dq[-1][0] < num:
                val, cnt = dq.pop()
                count += cnt
                cost += (num - val) * cnt

            dq.append((num, count))

            while cost > k:
                val, cnt = dq.popleft()
                cost -= val - nums[j]
                j -= 1

                if cnt > 1:
                    dq.appendleft((val, cnt - 1))

            ans += j - i + 1

        return ans