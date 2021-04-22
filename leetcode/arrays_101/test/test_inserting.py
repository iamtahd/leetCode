"""
Test suite for leetcode.arrays_101.in_place_ops.
https://leetcode.com/explore/learn/card/fun-with-arrays/511/in-place-operations/
"""
from leetcode.arrays_101.inserting import duplicateZeros
from leetcode.arrays_101.inserting import mergeSorted


def testDuplicateZeros():
    base = [1, 0, 2, 3, 0, 4, 5, 0]
    duplicateZeros(base)
    assert base == [1, 0, 0, 2, 3, 0, 0, 4]


def testMergeSortedArrays():
    nums1 = [1, 2, 3, 0, 0, 0]
    mergeSorted(nums1, m=3, nums2=[2, 5, 6], n=3)
    assert nums1 == [1, 2, 2, 3, 5, 6]
