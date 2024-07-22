#
# @lc app=leetcode id=268 lang=python3
#
# [268] Missing Number
#


# @lc code=start
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # sum of 0 to n - sum of nums = missing number
        # len(nums) = n
        # i = 0 to n - 1
        result = len(nums)

        for i in range(len(nums)):
            result += i - nums[i]

        return result


# @lc code=end
