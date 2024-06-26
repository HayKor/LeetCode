class Solution:
    def twoSum(self, nums: list[int], target: int):
        # Input: nums = [2, 7, 11, 15], target = 9
        # Output: [0, 1]
        hash = dict()
        for i in range(len(nums)):
            num = nums[i]
            remain = target - num
            if remain in hash:
                return [i, hash[remain]]
            hash[num] = i


sol = Solution()
print(sol.twoSum([2, 3, 5, 6, 7], 5))
print(sol.twoSum([0, 4, 3, 0], 0))
