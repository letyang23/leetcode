#
# @lc app=leetcode id=323 lang=python3
#
# [323] Number of Connected Components in an Undirected Graph
#

# @lc code=start
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i:[] for i in range(n)}
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        graphs = 0
        visit = set()

        def dfs(i):
            visit.add(i)
            for j in adj[i]:
                if j not in visit:
                    dfs(j)
        
        for i in range(n):
            if i not in visit:
                dfs(i)
                graphs+=1

        
        return graphs


# @lc code=end

