"""
Test suite for Leetcode Arrays 101: In-Place Operations
https://leetcode.com/explore/learn/card/fun-with-arrays/511/in-place-operations/
"""
from leetcode.arrays_101.in_place_ops import moveZeros
from leetcode.arrays_101.in_place_ops import sortArrayByParity
from leetcode.arrays_101.in_place_ops import replaceElements


def testReplaceElements():
    array = [17, 18, 5, 4, 6, 1]
    out = replaceElements(array)
    assert out == [18, 6, 6, 6, 1, -1]
    assert id(array) == id(out)


def testMoveZeros():
    array = [0, 1, 0, 3, 12]
    moveZeros(array)
    assert array == [1, 3, 12, 0, 0]


def testSortArrayByParity():
    array = [3, 1, 2, 4]
    out = sortArrayByParity(array)
    assert out == [2, 4, 3, 1]
    assert id(out) == id(array)
