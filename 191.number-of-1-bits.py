#
# @lc app=leetcode id=191 lang=python3
#
# [191] Number of 1 Bits
#

# @lc code=start
class Solution:
    def hammingWeight(self, n: int) -> int:
        result = 0
        while n:        # while n = while n>0 = while n!=0 
            result += n&1   # compare the last digit of n to 1
            n = n >> 1      # shift n to the right and compare again
        return result
# @lc code=end
