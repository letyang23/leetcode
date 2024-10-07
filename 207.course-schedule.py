#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#


# @lc code=start
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # preMap = {}
        # for i in range(numCourses):
        #     preMap[i] = []
        preMap = {i:[] for i in range(numCourses)}

        for course, prereq in prerequisites:
            preMap[course].append(prereq)

        visitedSet = set()

        def dfs(course):
            if course in visitedSet:
                return False
            if preMap[course] == []:
                return True

            visitedSet.add(course)
            for prereq in preMap[course]:
                if not dfs(prereq):
                    return False
            visitedSet.remove(course)
            preMap[course] = []
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
        return True


# @lc code=end
