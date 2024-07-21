#
# @lc app=leetcode id=153 lang=python3
#
# [153] Find Minimum in Rotated Sorted Array
#

# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        # Binary Search
        while l < r:
            m = l + (r-l) // 2
            if nums[m] > nums[r]:
                # search right part if middle is > right
                l = m + 1
            else:
                # search the left part is middle is < right
                r = m
        
        # return when left = right
        return nums[l]
# @lc code=end
