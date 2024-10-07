#
# @lc app=leetcode id=417 lang=python3
#
# [417] Pacific Atlantic Water Flow
#


# @lc code=start
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        ROWS, COLS = len(heights), len(heights[0])

        # pac = set of cell that can reach pacific
        # atl = set of cell that can reach atlantic
        pac, atl = set(), set()

        # dfs algorithm to exploring neighboring cells
        # (r, c) is the coordinates
        # visit is the set atl/pac
        # prevHeight is the Height of current cell (to be compared with neighboring cell)
        def dfs(r, c, visit, prevHeight):

            # conditions to stop exploring
            if (
                (r, c) in visit
                or r < 0
                or c < 0
                or r == ROWS
                or c == COLS
                or heights[r][c] < prevHeight
            ):
                return
            
            # cell is valid and add to the set
            visit.add((r, c))

            # exploring up, down, left, right cells
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])

        # exploring the edge (reach them = reach the ocean)
        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])
        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS - 1, atl, heights[r][COLS - 1])

        # result = pac & atl
        result = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    result.append([r, c])

        return result


# @lc code=end
