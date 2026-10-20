class Solution:
    def maxAlternatingSum(self, nums: list[int]) -> int:
        nums.sort(key=lambda x: x * x)
        mid = len(nums) // 2
        return sum(x * x for x in nums[mid:]) - sum(x * x for x in nums[:mid])