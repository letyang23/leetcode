#
# @lc app=leetcode id=381 lang=python3
#
# [381] Insert Delete GetRandom O(1) - Duplicates allowed
#

# @lc code=start
class RandomizedCollection:

    def __init__(self):
        self.values = []
        self.map = collections.defaultdict(list)

    def insert(self, val: int) -> bool:
        return True

    def remove(self, val: int) -> bool:
        return True

    def getRandom(self) -> int:
        return 1


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
# @lc code=end

