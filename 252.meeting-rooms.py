#
# @lc app=leetcode id=252 lang=python3
#
# [252] Meeting Rooms
#

# @lc code=start
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if not intervals:
            return True
        
        intervals.sort()
        prevInterval = [intervals[0]]
        for start, end in intervals[1:]:
            lastEnd = prevInterval[-1][1]
            if start < lastEnd:
                return False
            else:
                prevInterval.append([start, end])
        
        return True

# @lc code=end

