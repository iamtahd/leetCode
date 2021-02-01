from copy import copy

import leetcode.arrays as arrays


# Accessing Arrays
def testLongestOnes():
    assert arrays.findMaxConsecutiveOnes([]) == 0
    assert arrays.findMaxConsecutiveOnes([0, 0, 0]) == 0
    assert arrays.findMaxConsecutiveOnes([1, 1]) == 2
    assert arrays.findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]) == 3


def testFindNums():
    assert arrays.findNumbers([555, 901, 482, 1771]) == 1
    assert arrays.findNumbers([12, 345, 2, 6, 7896]) == 2


def testSortedSquares():
    assert arrays.sortedSquares([-4, -1, 0, 3, 10]) == [0, 1, 9, 16, 100]


# Inserting Items into an Array
def testDuplicateZeros():
    base = [1, 0, 2, 3, 0, 4, 5, 0]
    ans = [1, 0, 0, 2, 3, 0, 0, 4]
    clever = copy(base)
    simple = copy(base)

    arrays.duplicateZeros(base)
    arrays.duplicateZerosClever(clever)
    arrays.duplicateZerosSimple(simple)
    assert base == clever == simple == ans


def testMergeSortedArrays():
    nums1 = [1, 2, 3, 0, 0, 0]
    arrays.mergeSorted(nums1, m=3, nums2=[2, 5, 6], n=3)
    assert nums1 == [1, 2, 2, 3, 5, 6]


# Deleting Items from an array
def testRemoveElement():
    assert arrays.removeElement([3, 2, 2, 3], 3) == 2
    assert arrays.removeElementWhile([3, 2, 2, 3], 3) == 2


def testRemoveDuplicates():
    assert arrays.removeDuplicates([1, 1, 2]) == 2
    assert arrays.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]) == 5


# Searching for Items in an Array
