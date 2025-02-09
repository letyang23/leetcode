from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsDict = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in numsDict:
                return [numsDict[diff], i]
            numsDict[nums[i]] = i
# leetcode submit region end(Prohibit modification and deletion)

solution = Solution()
print(solution.twoSum([2, 7, 11, 15], 9))