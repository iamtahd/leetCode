"""
Test suite for Leetcode Arrays 101: Deleting Items From an Array
https://leetcode.com/explore/learn/card/fun-with-arrays/526/deleting-items-from-an-array/3246/
"""
from leetcode.arrays_101.deleting import removeElement
from leetcode.arrays_101.deleting import removeDuplicates


def testRemoveElement():
    assert removeElement([3, 2, 2, 3], 3) == 2


def testRemoveDuplicates():
    assert removeDuplicates([1, 1, 2]) == 2
    assert removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]) == 5
