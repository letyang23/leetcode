#
# @lc app=leetcode id=152 lang=python3
#
# [152] Maximum Product Subarray
#

# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxProd = max(nums) 
        currMax, currMin = 1, 1

        for n in nums:
            tmp = n * currMax
            currMax = max(n * currMax, n * currMin, n)
            currMin = min(tmp, n * currMin, n)
            maxProd = max(currMax, maxProd)
        
        return maxProd
# @lc code=end

