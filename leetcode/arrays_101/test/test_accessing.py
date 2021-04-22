"""
Test suite for Leetcode Arrays 101: Accessing Arrays
https://leetcode.com/explore/learn/card/fun-with-arrays/521/introduction/3238/
"""
from leetcode.arrays_101.accessing import findNumbers
from leetcode.arrays_101.accessing import findMaxConsecutiveOnes
from leetcode.arrays_101.accessing import sortedSquares


def testFindMaxConsecutiveOnes():
    assert findMaxConsecutiveOnes([]) == 0
    assert findMaxConsecutiveOnes([0, 0, 0]) == 0
    assert findMaxConsecutiveOnes([1, 1]) == 2
    assert findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]) == 3


def testFindNums():
    assert findNumbers([555, 901, 482, 1771]) == 1
    assert findNumbers([12, 345, 2, 6, 7896]) == 2


def testSortedSquares():
    assert sortedSquares([-4, -1, 0, 3, 10]) == [0, 1, 9, 16, 100]



