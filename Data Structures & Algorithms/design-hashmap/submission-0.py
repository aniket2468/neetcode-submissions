class MyHashMap:
    class Node:
        __slots__ = ("key", "val", "next")
        def __init__(self, key: int, val: int, nxt=None):
            self.key = key
            self.val = val
            self.next = nxt

    def __init__(self):
        self.N = 2069  # prime bucket size
        self.buckets = [None] * self.N

    def _idx(self, key: int) -> int:
        return key % self.N

    def put(self, key: int, value: int) -> None:
        i = self._idx(key)
        head = self.buckets[i]
        cur = head

        while cur:
            if cur.key == key:
                cur.val = value
                return
            cur = cur.next

        # insert new node at head
        self.buckets[i] = self.Node(key, value, head)

    def get(self, key: int) -> int:
        i = self._idx(key)
        cur = self.buckets[i]

        while cur:
            if cur.key == key:
                return cur.val
            cur = cur.next

        return -1

    def remove(self, key: int) -> None:
        i = self._idx(key)
        cur = self.buckets[i]
        prev = None

        while cur:
            if cur.key == key:
                if prev is None:
                    self.buckets[i] = cur.next
                else:
                    prev.next = cur.next
                return
            prev = cur
            cur = cur.next
