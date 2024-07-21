#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        # we want to first sort the input array
        # because we need to eliminate duplicates
        # and use left,right pointer to do two sum later
        nums.sort()

        for i, num in enumerate(nums):
            
            # skip the duplicate
            if i > 0 and num = nums[i-1]:
                continue
            

        return result
# @lc code=end

