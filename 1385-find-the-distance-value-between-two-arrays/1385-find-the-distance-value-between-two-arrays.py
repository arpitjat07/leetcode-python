from bisect import bisect_left

class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        arr2.sort()
        ans = 0

        for x in arr1:
            i = bisect_left(arr2, x)

            if (i == len(arr2) or arr2[i] - x > d) and \
               (i == 0 or x - arr2[i - 1] > d):
                ans += 1

        return ans