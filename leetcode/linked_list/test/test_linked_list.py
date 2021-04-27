"""
Test suite for Leetcode Linked List: Singly Linked List
https://leetcode.com/explore/learn/card/linked-list/209/singly-linked-list/1290/
"""
import pytest

from leetcode.linked_list.linked_list import MyLinkedList


@pytest.fixture
def linkedList() -> MyLinkedList:
    return MyLinkedList.fromSequence([1, 2, 3, 4, 5])


def testGet(linkedList):
    assert linkedList.get(3) == 4
    assert linkedList.get(5) == -1


def testAddAtHead(linkedList):
    addedVal = 10
    linkedList.addAtHead(addedVal)
    assert linkedList.get(0) == addedVal


def testAddAtTail(linkedList):
    addedVal = 10
    linkedList.addAtTail(addedVal)
    assert linkedList.get(5) == addedVal


def testAddAtIndex(linkedList):
    linkedList.addAtIndex(3, 100)
    assert linkedList.get(3) == 100


def testDeleteAtIndex(linkedList):
    linkedList.deleteAtIndex(3)
    assert linkedList.get(3) == 5

    linkedList = MyLinkedList()
    linkedList.deleteAtIndex(0)
    assert linkedList.get(0) == -1


def testScenario():
    linkedList = MyLinkedList()
    linkedList.addAtHead(1)
    linkedList.addAtTail(3)
    linkedList.addAtIndex(1, 2)
    assert linkedList.get(1) == 2
    linkedList.deleteAtIndex(1)
    assert linkedList.get(1) == 3


def testHasCycle():
    linkedList = MyLinkedList.fromSequence([3, 2, 0, -4])
    linkedList.connectTailToIndex(1)
    assert linkedList.hasCycle(head=linkedList.head)

    linkedList = MyLinkedList.fromSequence([1, 2])
    linkedList.connectTailToIndex(0)
    assert linkedList.hasCycle(head=linkedList.head)

    linkedList = MyLinkedList.fromSequence([1])
    assert not linkedList.hasCycle(head=linkedList.head)


def testDetectCycle_Floyd():
    linkedList = MyLinkedList.fromSequence([3, 2, 0, -4])
    linkedList.connectTailToIndex(1)
    connector = linkedList.head.next
    assert linkedList.detectCycle_Floyd(head=linkedList.head) == connector


def testDetectCycle_HashTable():
    linkedList = MyLinkedList.fromSequence([3, 2, 0, -4])
    linkedList.connectTailToIndex(1)
    connector = linkedList.head.next
    assert linkedList.detectCycle_Hash(head=linkedList.head) == connector
