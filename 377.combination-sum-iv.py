#
# @lc app=leetcode id=377 lang=python3
#
# [377] Combination Sum IV
#


# @lc code=start
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1
        # dp[i]是i有几种方法可以combine
        for i in range(1, target + 1):
            for j in range(len(nums)):
                if i >= nums[j]:
                    dp[i] += dp[i - nums[j]]

        return dp[target]


# @lc code=end
