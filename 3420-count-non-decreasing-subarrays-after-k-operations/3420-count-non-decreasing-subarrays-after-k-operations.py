from collections import deque
from typing import List

class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
        dq = deque()
        j = len(nums) - 1
        cost = ans = 0

        for i in range(len(nums) - 1, -1, -1):
            x = nums[i]
            cnt = 1

            while dq and dq[-1][0] < x:
                v, c = dq.pop()
                cnt += c
                cost += (x - v) * c

            dq.append((x, cnt))

            while cost > k:
                v, c = dq.popleft()
                cost -= v - nums[j]
                j -= 1

                if c > 1:
                    dq.appendleft((v, c - 1))

            ans += j - i + 1

        return ans