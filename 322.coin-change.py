#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#


# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # create a dp array and initialize all entries (except 0) to amount + 1
        # (a value greater than the max possible coins needed)
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        # Iterate through all amounts from "1" to "amount"
        for a in range(1, amount + 1):

            # For each amount, check each coin
            for c in coins:
                
                # If the coin c can be used (i.e., a - c >= 0)
                # update dp[a] to be the minimum of its current value or 1 + dp[a - c].
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c])
                    
                    # Example:
                    # coin = 4, amount = 7
                    # dp[7] = 1 + dp[3]

        return dp[amount] if dp[amount] != amount + 1 else -1
        # @lc code=end
