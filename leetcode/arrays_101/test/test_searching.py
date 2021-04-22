"""
Test suite for Leetcode Arrays 101: Searching For Items In An Array
https://leetcode.com/explore/learn/card/fun-with-arrays/527/searching-for-items-in-an-array/3296/
"""
from leetcode.arrays_101.searching import checkIfExist
from leetcode.arrays_101.searching import isMountainArray


def testIfExist():
    assert checkIfExist([10, 2, 5, 3]) is True
    assert checkIfExist([7, 1, 14, 11]) is True
    assert checkIfExist([3, 1, 7, 11]) is False
    assert checkIfExist([-2, 0, 10, -19, 4, 6, -8]) is False
    assert checkIfExist([0, 0]) is True


def testValidMountainArray():
    assert isMountainArray([1, 2]) is False
    assert isMountainArray([3, 5, 5]) is False
    assert isMountainArray([0, 3, 2, 1]) is True
    assert isMountainArray([0, 2, 3, 4, 5, 2, 1, 0]) is True
    assert isMountainArray([0, 2, 3, 3, 5, 2, 1, 0]) is False
    assert isMountainArray([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) is False
