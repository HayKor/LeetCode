class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        r = n - k
        moved = nums[0:r]
        nums[0:r] = []
        nums.extend(moved)


sol = Solution()
nums = [1, 2, 3, 4, 5, 6, 7]
sol.rotate(nums, -2)
print(nums)
sol.rotate(nums, 2)
print(nums)
sol.rotate(nums, 2)
print(nums)
