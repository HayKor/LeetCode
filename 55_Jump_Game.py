class Solution:
    def canJump(self, nums: list[int]) -> bool:
        # nums = [2,3,1,1,4]
        fuel = 0
        for num in nums:
            if fuel < 0:
                return False
            if num > fuel:
                fuel = num
            fuel -= 1
        return True


sol = Solution()
print(sol.canJump([2, 3, 1, 1, 4]))
print(sol.canJump([3, 2, 1, 0, 4]))
