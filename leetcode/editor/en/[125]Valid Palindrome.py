
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Two pointer solution
        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not self.alphanum(s[l]):
                l += 1
            while r > l and not self.alphanum(s[r]):
                r -= 1
            # not palindrome
            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1

        return True

    # Use ASCII Value to determine if the char is an alphanumeric char
    def alphanum(self, c:str):
        return (ord('A') <= ord(c) <= ord('Z')
                or ord('0') <= ord(c) <= ord('9')
                or ord('a') <= ord(c) <= ord('z'))
# leetcode submit region end(Prohibit modification and deletion)

solution = Solution()
print(solution.isPalindrome("ab_a"))
