#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#


# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Does it have a left neighbor?
        # if it doesn't, it is a start of a sequence

        # convert into a set

        # why make it a set?
        # "In python, set is implemented as a hash table.
        # So you can expect to lookup/insert/delete in O(1) average."
        numSet = set(nums)
        longest = 0

        for n in nums:
            # check if its the start of a sequence
            if (n - 1) not in nums:
                length = 0
                while (n + length) in nums:
                    length += 1
                longest = max(length, longest)
        return longest


# @lc code=end
