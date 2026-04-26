class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # nums = [9,1,4,2,3,3,7]
        # output: 4

        LIS = [1]*len(nums)

        for i in range(len(nums) - 1, -1, -1):
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])
        return max(LIS)
