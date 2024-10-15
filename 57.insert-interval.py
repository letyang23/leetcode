#
# @lc app=leetcode id=57 lang=python3
#
# [57] Insert Interval
#

# @lc code=start
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []

        for i in range(len(intervals)):
            # Case 1: No overlap, and newInterval goes before the current interval
            if newInterval[1] < intervals[i][0]:
                result.append(newInterval)
                return result + intervals[i:]
            
            # Case 2: No overlap, and newInterval goes after the current interval
            elif newInterval[0] > intervals[i][1]:
                result.append(intervals[i])

            # Case 3: Overlapping intervals - merge to newInterval
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
        
        result.append(newInterval)

        return result
# @lc code=end

