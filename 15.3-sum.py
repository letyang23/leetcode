#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#


# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        # we want to first sort the input array
        # because we need to eliminate duplicates
        # and use left,right pointer to do two sum later
        nums.sort()

        for i, num in enumerate(nums):

            # skip the duplicate
            if i > 0 and num == nums[i - 1]:
                continue

            # easier way to do twoSum when the list is sorted
            # use left and right Two-Pointer
            left, right = i + 1, len(nums) - 1
            while left < right:
                threeSum = num + nums[left] + nums[right]
                if threeSum > 0:
                    right -= 1
                elif threeSum < 0:
                    left += 1
                else:
                    result.append([num, nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1

        return result


# @lc code=end
