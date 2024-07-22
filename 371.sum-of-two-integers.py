#
# @lc app=leetcode id=371 lang=python3
#
# [371] Sum of Two Integers
#

# @lc code=start
class Solution:
    def getSum(self, a: int, b: int) -> int:
        # 1+2 = 01+10 = 11 = 3
        # 2+3 = 10+11 = 101 = 5
        # First we need to use XOR to figure out the adding
        # Then we use AND with shift to left 1 (<< 1) to figure out the carry
        # In the end add them together (same operation)
        while b != 0:
            old_a = a
            a = a ^ b
            b = (old_a&b) << 1
        return a
# @lc code=end

