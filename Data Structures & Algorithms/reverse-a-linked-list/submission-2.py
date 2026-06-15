# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        revNode = None

        while head:
            next = head.next
            head.next = revNode
            revNode = head
            head = next
        
        return revNode