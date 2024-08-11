#
# @lc app=leetcode id=1143 lang=python3
#
# [1143] Longest Common Subsequence
#


# @lc code=start
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Example: text1 : a b c d e text2: a c e
        # 1. create 2d DP array [x][y]
        # 2. if a = a, then [x+1][y+1] (going diagonal)
        # 3. if b != c, then [x+1][y] or [x][y+1] (go down or go right)
        # 4. at end, we put 0 when we out of bounds.

        dp = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]

        for i in range(0, len(text1)):
            for j in range(0, len(text2)):
                if text1[i] == text2[j]:
                    dp[i + 1][j + 1] = 1 + dp[i][j]
                else:
                    dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])
        return dp[len(text1)][len(text2)]


# @lc code=end
