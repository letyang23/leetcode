#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#


# @lc code=start
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
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                mergedLists.append(self.merge(l1, l2))
            lists = mergedLists
        return lists[0]

    def merge(self, list1, list2):
        # using leetcode 21 solution - merge 2 sorted lists
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


# @lc code=end
