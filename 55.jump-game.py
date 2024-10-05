#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#


# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1  # goal at the end of array

        for i in range(len(nums) - 1, -1, -1):  # start at the last index
            if i + nums[i] >= goal:  # it means we can reach the goal
                goal = i  # shift the goal closer to the start point

        return (
            True if goal == 0 else False
        )  # if goal = 0 then we can reach the end else no we can't


# @lc code=end
