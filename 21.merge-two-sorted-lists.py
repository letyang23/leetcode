#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
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

