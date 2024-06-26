class Solution:
    def twoSum(self, nums: list[int], target: int):
        # Input: nums = [2,7,11,15], target = 9
        # Output: [0,1]
        # nums = list(filter(lambda x: x <= target, nums))
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


sol = Solution()
print(sol.twoSum([2, 3, 5, 6, 7], 5))
print(sol.twoSum([0, 4, 3, 0], 0))
