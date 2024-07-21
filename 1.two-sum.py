#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # create a dictionary
        numsDict = {}
        
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in numsDict:
                return[numsDict[diff], i]
            numsDict[nums[i]] = i
        return
# @lc code=end

