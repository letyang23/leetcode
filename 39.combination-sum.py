#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#

# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        
        # i 是 index of the candidate, cur 是 output list，total 是 target
        def dfs(i, cur, total):
            # Base case
            if total == target:
                result.append(cur.copy())
                return
            # if i is out of bounds
            if i >= len(candidates) or total > target:
                return
            
            cur.append(candidates[i])
            dfs(i, cur, total + candidates[i])
            cur.pop()
            dfs(i + 1, cur, total)
        
        dfs(0, [], 0)
        return result
# @lc code=end

