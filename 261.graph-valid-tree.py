#
# @lc app=leetcode id=261 lang=python3
#
# [261] Graph Valid Tree
#


# @lc code=start
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True

        adj = {i: [] for i in range(n)}  # Create a hashset
        for n1, n2 in edges:    # using the hashset to record all of neighbors
            adj[n1].append(n2)
            adj[n2].append(n1)

        visit = set()  # visit set

        def dfs(i, prev):  # record prev for loop detection
            if i in visit:
                return False

            visit.add(i)
            for j in adj[i]:
                if j == prev:
                    continue
                if not dfs(j, i):
                    return False
            return True

        return dfs(0, -1) and n == len(visit)


# @lc code=end
