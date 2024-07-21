#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # O(log n) means binary search
        # nums has two sorted part of array

        # example : [4,5,6,7,0,1,2]
        # left portion: [4,5,6,7]
        # right portion: [0, 1, 2]

        left, right = 0, len(nums)-1
        while left <= right:
            middle = left+(right-left)//2

            if target == nums[middle]:
                return middle

            # middle pointer is in the left portion
            if nums[middle] >= nums[left]:

                if target > nums[middle] or target < nums[left]:
                    # target is on the right
                    left = middle + 1
                else:
                    # target is on the left
                    right = middle - 1
                
            # middle is in the right portion
            else:
                if target < nums[middle] or target > nums[right]:
                    # search left
                    right = middle - 1
                else: 
                    # search right
                    left = middle + 1
        # can't find it
        return -1

# @lc code=end

