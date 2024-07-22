#
# @lc app=leetcode id=338 lang=python3
#
# [338] Counting Bits
#

# @lc code=start
class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(n+1):
            result = 0
            while i:
                result += i&1
                i = i >> 1
            ans.append(result)
        
        return ans
# @lc code=end

