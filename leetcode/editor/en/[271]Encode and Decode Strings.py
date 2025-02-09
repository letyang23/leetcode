class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """

    # strs = "[neet, co#de]"

    def encode(self, strs):
        # write your code here
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    # res = "4#neet5#co#de"

    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    """

    def decode(self, str):
        # write your code here
        res, i = [], 0

        while i < len(str):
            j = i
            while str[j] != "#":
                j += 1
            length = int(str[i:j])
            res.append(str[j + 1: j + 1 + length])
            i = j + 1 + length

        return res

solution = Solution()
new_str = solution.encode(["neet", "code"])
print(new_str)
print(solution.decode(new_str))
