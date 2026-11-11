class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        mn = min(need1, need2)
        mx = max(need1, need2)

        a = need1 * cost1 + need2 * cost2
        b = mn * costBoth + (need1 - mn) * cost1 + (need2 - mn) * cost2
        c = mx * costBoth

        return min(a, b, c)