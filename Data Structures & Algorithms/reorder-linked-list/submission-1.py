# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        arr = []
        cur = head

        while cur:
            arr.append(cur.val)
            cur = cur.next
        
        cur = head
        for i in range(len(arr)):
            if i % 2 == 0:
                cur.val = arr[i // 2]
            else:
                cur.val = arr[len(arr) - (i + 1) // 2]
            
            cur = cur.next
        return 
