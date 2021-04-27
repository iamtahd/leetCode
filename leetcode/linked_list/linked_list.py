"""
Leetcode Linked List: Singly Linked List
https://leetcode.com/explore/learn/card/linked-list/209/singly-linked-list/1290/
"""
from typing import Optional, List


class Node:
    """Singly linked item within MyLinkedList."""

    def __init__(self, val: int, next_: Optional["Node"] = None):
        self.val = val
        self.next = next_

    def __str__(self):
        return f'{self.val}'

    def __repr__(self) -> str:
        return f'{self.val}'


class MyLinkedList:
    """Simple, singly linked list."""

    def __init__(self):
        self.head = None
        self.size = 0

    def __repr__(self) -> str:
        """

        :return:
        """
        nodes = []
        curr = self.head
        for i in range(self.size):
            nodes.append(curr)
            curr = curr.next
        return str(nodes)

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the
        index is invalid, return -1.

        :param index: linked list location to return if possible
        :return: value of the node at the given index or -1
        """
        if index < 0 or index >= self.size:
            return -1

        curr = self.head
        for i in range(index):
            curr = curr.next
        return curr.val

    @classmethod
    def fromSequence(cls, sequence: List[int]) -> "MyLinkedList":
        """
        Constructs a populated LinkedList with a Node for each value in the
        given list.

        :param sequence: list of ints to generate a linked list from
        :return: new instance
        """
        instance = cls()
        for val in sequence:
            instance.addAtTail(val)
        return instance

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val as the last element of the linked list.

        :param val: value for the new Node at the end of the list
        :return: None
        """
        if self.head is None:
            self.head = Node(val)
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next

            curr.next = Node(val)
        self.size += 1

    def connectTailToIndex(self, index: int) -> None:
        """
        Create a loop from the tail node to a node at a given index.

        :param index: position of the node to link the tail node to
        :return: None
        """
        if index < 0 or index > self.size:
            return

        curr = self.head
        connector = None
        for i in range(self.size-1):
            if i == index:
                connector = curr
            curr = curr.next

        curr.next = connector

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list.
        After the insertion, the new node will be the first node of the linked list.

        :param val: value of the node to add as the new head
        :return: None
        """
        node = Node(val)
        node.next = self.head
        self.head = node
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        """

        :param index:
        :param val:
        :return:
        """
        if index < 0 or index > self.size:
            return

        if index == 0:
            self.addAtHead(val)
        else:
            curr = self.head
            for i in range(index-1):
                curr = curr.next
            node = Node(val)
            node.next = curr.next
            curr.next = node
            self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        :param index: node position to remove from list
        :return: None
        """
        if index < 0 or index >= self.size:
            return

        curr = self.head
        if index == 0:
            self.head = curr.next
        else:
            curr = self.head
            for i in range(index-1):
                curr = curr.next
            curr.next = curr.next.next
        self.size -= 1

    @staticmethod
    def hasCycle(head: Node) -> bool:
        """
        Given head, the head of a linked list, determine if the linked list has
        a cycle in it.

        There is a cycle in a linked list if there is some node in the list
        that can be reached again by continuously following the next pointer.
        Internally, pos is used to denote the index of the node that tail's
        next pointer is connected to. Note that pos is not passed as a parameter.

        :param head:
        :return: true if there is a cycle in the linked list. Otherwise, return false.
        """
        if not head:
            return False

        slow = head
        fast = head.next

        while fast != slow:
            if fast is None or fast.next is None:
                return False
            fast = fast.next.next
            slow = slow.next

        return True

    @staticmethod
    def detectCycle_Floyd(head: Node) -> Optional[Node]:
        """
        Given a linked list, return the node where the cycle begins. If there is
        no cycle, return null.

        There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

        Notice that you should not modify the linked list.

        Floyd's Tortoise and Hare approach.

        :param head: starting node of the linkedList
        :return Node where the linkedList connects to itself or None if there is no cycle
        """

        def getIntersection(node):
            tortoise = node
            hare = node

            while hare is not None and hare.next is not None:
                tortoise = tortoise.next
                hare = hare.next.next
                if tortoise == hare:
                    return tortoise
            return None

        if not head:
            return None

        intersect = getIntersection(head)
        if intersect is None:
            return None

        pointer1 = head
        pointer2 = intersect

        while pointer1 != pointer2:
            pointer1 = pointer1.next
            pointer2 = pointer2.next

        return pointer1

    @staticmethod
    def detectCycle_Hash(head: Node) -> Optional[Node]:
        """
        Given a linked list, return the node where the cycle begins. If there is
        no cycle, return null.

        There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

        Notice that you should not modify the linked list.

        **HASH TABLE APPROACH**
        This is conceptually more simple but has:
            O(n) space-complexity (Floyd has O(1))
            O(n) time-complexity  (Floyd has O(n))

        :param head: starting node of the linkedList
        :return Node where the linkedList connects to itself or None if there is no cycle
        """
        visited = set()

        node = head
        while node is not None:
            if node in visited:
                return node
            else:
                visited.add(node)
                node = node.next
        return None












