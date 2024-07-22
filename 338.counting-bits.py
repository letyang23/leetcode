#
# @lc app=leetcode id=338 lang=python3
#
# [338] Counting Bits
#


# @lc code=start
class Solution:
    def countBits(self, n: int) -> List[int]:
        # Initialize dp array with zeros
        dp = [0] * (n + 1)

        # Initialize offset to 1 (the first power of 2)
        offset = 1

        # Loop from 1 to n to fill dp array
        for i in range(1, n + 1):

            # Check if i is a new power of 2
            if offset * 2 == i:
                offset = i
                
            # Calculate the number of 1's for current i
            dp[i] = 1 + dp[i - offset]

        return dp


# @lc code=end
