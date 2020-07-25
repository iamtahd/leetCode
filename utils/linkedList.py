
class LinkedList:
    def __init__(self, sequence):
        self.head = ListNode(sequence[0])
        current = self.head
        for item in sequence[1:]:
            current.next = ListNode(item)
            current = current.next


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
