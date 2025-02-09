from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None

        while len(lists) > 1:
            mergedLists = []

            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None
                mergedLists.append(self.merge(l1, l2))
            lists = mergedLists
        return lists[0]

    def merge(self, list1, list2):
        prevNode = ListNode(-1)
        tmp = prevNode

        while list1 or list2:
            if list1 is None:
                tmp.next = list2
                break
            if list2 is None:
                tmp.next = list1
                break
            if list1.val <= list2.val:
                tmp.next = list1
                tmp = list1
                list1 = list1.next
            else:
                tmp.next = list2
                tmp = list2
                list2 = list2.next
        return prevNode.next


# leetcode submit region end(Prohibit modification and deletion)

# Helper function to convert a list to a linked list.
def list_to_linkedlist(lst):
    dummy = ListNode(0)
    current = dummy
    for num in lst:
        current.next = ListNode(num)
        current = current.next
    return dummy.next


# Helper function to convert a linked list to a list.
def linkedlist_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result


# Creating input test case
lists_input = [[1, 4, 5], [1, 3, 4], [2, 6]]
linked_lists = [list_to_linkedlist(lst) for lst in lists_input]

# Testing the solution function
solution = Solution()
merged_head = solution.mergeKLists(linked_lists)

# Printing the result (after implementing mergeKLists, it should print the merged sorted list)
print(linkedlist_to_list(merged_head))
