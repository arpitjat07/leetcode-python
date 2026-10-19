class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        less = sum(x < target for x in nums)
        equal = sum(x == target for x in nums)
        return list(range(less, less + equal))