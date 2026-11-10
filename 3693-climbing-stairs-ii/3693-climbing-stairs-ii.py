class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        a = b = c = 0

        for x in costs:
            a, b, c = b, c, x + min(c + 1, b + 4, a + 9)

        return c