from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Recursion DFS Solution
        # if not root:
        #     return 0
        #
        # return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

        # BFS (Using Queue)
        # if not root:
        #     return 0
        #
        # level = 0
        # q = deque([root])
        # while q:
        #
        #     for i in range(len(q)):
        #         node = q.popleft()
        #         if node.left:
        #             q.append(node.left)
        #         if node.right:
        #             q.append(node.right)
        #
        #     level += 1
        # return level

        # Iterative DFS
        stack = [[root, 1]]
        res = 0

        while stack:
            node, depth = stack.pop()

            if node:
                res = max(res, depth)
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])
        return res


# leetcode submit region end(Prohibit modification and deletion)

# Helper Function
def to_binary_tree(items):
    if not items:
        return None

    it = iter(items)
    root = TreeNode(next(it))
    q = [root]
    for node in q:
        val = next(it, None)
        if val is not None:
            node.left = TreeNode(val)
            q.append(node.left)
        val = next(it, None)
        if val is not None:
            node.right = TreeNode(val)
            q.append(node.right)
    return root

# Test Case
node = [3,9,20,None,None,15,7]
root = to_binary_tree(node)
solution = Solution()
print(solution.maxDepth(root))