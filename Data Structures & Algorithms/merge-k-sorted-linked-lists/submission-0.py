# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        h = []
        for i, node in enumerate(lists):
            heapq.heappush(h, (node.val, i, node))

        dummy = ListNode(0)
        tail = dummy

        while h:
            _, i, node = heapq.heappop(h)
            tail.next = node
            tail = tail.next

            if node.next:
                heapq.heappush(h, (node.next.val, i, node.next))
        return dummy.next