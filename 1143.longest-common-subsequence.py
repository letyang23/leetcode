#
# @lc app=leetcode id=1143 lang=python3
#
# [1143] Longest Common Subsequence
#

# @lc code=start
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        answer = []
        for i in range(len(text1)):
            for j in range(len(text2)):
                if text1[i] == text2[j]:
                    answer.append(text1[i])
        return len(answer)
# @lc code=end

