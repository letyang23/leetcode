from collections import defaultdict
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(s)

        return list(ans.values())
# leetcode submit region end(Prohibit modification and deletion)

solution = Solution()
print(solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))