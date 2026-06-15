# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        num = 0
        while head:
            num += 1
            head = head.next
        
        n_from_front = num - n

        # left = dummy

        while n_from_front > 0:
            left = left.next
            n_from_front -= 1
        

        left.next = left.next.next

        return dummy.next