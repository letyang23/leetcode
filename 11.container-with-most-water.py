#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        result = 0
        left, right = 0, len(height)-1
        while left < right:
            yaxis = min(height[left],height[right])
            xaxis = right-left
            area = yaxis*xaxis
            if area > result:
                result = area

            if height[right]> height[left]:
                left += 1
            else:
                right -= 1
            
        return result



# @lc code=end

