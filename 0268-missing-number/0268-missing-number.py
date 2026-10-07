class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        sm = 0
        for i in range(0,len(nums)):
            sm += nums[i]
        x = len(nums)
        x = x*(x+1)/2
        return int(x-sm)