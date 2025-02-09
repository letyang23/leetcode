
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = 0

        for i in range(len(s)):
            l = r = i
            ans += self.countPali(s, l, r)

            l = i
            r = i + 1
            ans += self.countPali(s, l, r)
        return ans

    def countPali(self, s, l, r):
        res = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            res += 1
            l -= 1
            r += 1
        return res
# leetcode submit region end(Prohibit modification and deletion)


solution = Solution()
print(solution.countSubstrings("aaa"))