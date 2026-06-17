class Solution:
    def missingNumber(self, nums):
        n = len(nums)
        return n * (n + 1) // 2 - sum(nums)

nums = [3, 0, 1]

obj = Solution()

print(obj.missingNumber(nums))