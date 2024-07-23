#
# @lc app=leetcode id=190 lang=python3
#
# [190] Reverse Bits
#

# @lc code=start
class Solution:
    def reverseBits(self, n: int) -> int:
        # AND with 1
        # and then shift 1 to the left <<
        result = 0

        for _ in range(32):
            result = (result << 1) + (n&1)
            n = n >> 1
        
        return result
    
# @lc code=end

