#
# @lc app=leetcode id=323 lang=python3
#
# [323] Number of Connected Components in an Undirected Graph
#


# @lc code=start
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # 2. Union-find method
        parent = [i for i in range(n)]
        rank = [1] * n

        def find(n1):
            result = n1

            while result != parent[result]:
                parent[result] = parent[parent[result]]
                result = parent[result]
            return result

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return 0

            if rank[p2] > rank[p1]:
                parent[p1] = p2
                rank[p2] += rank[p1]
            else:
                parent[p2] = p1
                rank[p1] += rank[p2]
            return 1

        result = n
        for n1, n2 in edges:
            result -= union(n1, n2)
        return result

        # 1. My DFS Way
        # adj = {i:[] for i in range(n)}
        # for n1, n2 in edges:
        #     adj[n1].append(n2)
        #     adj[n2].append(n1)

        # graphs = 0
        # visit = set()

        # def dfs(i):
        #     visit.add(i)
        #     for j in adj[i]:
        #         if j not in visit:
        #             dfs(j)

        # for i in range(n):
        #     if i not in visit:
        #         dfs(i)
        #         graphs+=1

        # return graphs


# @lc code=end
