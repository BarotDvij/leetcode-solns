# Last updated: 10/15/2025, 3:02:51 AM
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        dp = ListNode(0, head)
        slow = head
        fast = head
        last = dp

        while fast and fast.next:
            last = slow
            slow = slow.next
            fast = fast.next.next
        last.next = slow.next
        return dp.next
        