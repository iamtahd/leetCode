class LinkedList:
    def __init__(self, sequence):
        if not sequence:
            self.head = None
        else:
            self.head = ListNode(sequence[0])
            current = self.head
            for item in sequence[1:]:
                current.next = ListNode(item)
                current = current.next


class ListNode:
    def __init__(self, x=0, next_=None):
        self.val = x
        self.next = next_
