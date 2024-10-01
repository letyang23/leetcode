from typing import List


def findLongestSubarray(arr: List[int], limit: int) -> int:
    stack = []
    left = [0] * len(arr)
    right = [0] * len(arr)

    # Fill left array
    for i in range(len(arr)):
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()
        left[i] = stack[-1] if stack else -1
        stack.append(i)

    # Clear the stack for reuse
    stack.clear()

    # Fill right array
    for i in range(len(arr) - 1, -1, -1):
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()
        right[i] = stack[-1] if stack else len(arr)
        stack.append(i)

    maxLength = -1

    # Calculate the maximum length of the good subarray
    for i in range(len(arr)):
        length = right[i] - left[i] - 1
        if arr[i] * length > limit:
            maxLength = max(maxLength, length)

    return maxLength


arr = [1, 3, 4, 3, 1]
limit = 6
result = findLongestSubarray(arr, limit)
print(result)
