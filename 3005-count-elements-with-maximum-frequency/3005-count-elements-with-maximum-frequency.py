class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        nums = sorted(nums)
        i = 0
        mx = 0
        mx_n = 0
        while i<len(nums):
            count = 1
            for j in range(i+1,len(nums)):
                if(nums[i]==nums[j]):
                    count += 1
                else:
                    break
            if(count == mx):
                mx_n += mx
            if(count > mx):
                mx = count
                mx_n = mx
            i += count
        return mx_n
            