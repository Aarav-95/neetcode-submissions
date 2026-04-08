class ListNode:
    def __init__(self, val=None, key=None):
        self.val = val
        self.key = key
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.head = ListNode()
        self.tail = ListNode()
        self.pairs = {}
        self.max_size = capacity

        self.head.next = self.tail
        self.tail.prev = self.head
    def _remove(self, node: ListNode):
        prev, next = node.prev, node.next
        prev.next = next
        next.prev = prev
    def _append(self, node: ListNode):
        prev = self.tail.prev
        prev.next = node
        node.prev = prev
        node.next = self.tail
        self.tail.prev = node

    def get(self, key: int) -> int:
        if key not in self.pairs:
            return -1
        remove = self.pairs[key]
        self._remove(remove)
        self._append(remove)
        return remove.val
    def put(self, key: int, value: int) -> None:
        if key in self.pairs:
            node = self.pairs[key]
            node.val = value
            self._remove(node)
            self._append(node)
        else:
            temp = ListNode(value, key)
            self.pairs[key] = temp
            self._append(temp)
            if len(self.pairs) > self.max_size:
                lru = self.head.next
                self._remove(lru)
                del self.pairs[lru.key]


