"""
Leetcode Arrays 101: Inserting Items Into An Array
https://leetcode.com/explore/learn/card/fun-with-arrays/525/inserting-items-into-an-array/3244/
"""
from typing import List


def duplicateZeros(arr: List[int]) -> None:
    """
    Given a fixed length array arr of integers, duplicate each occurrence of zero, shifting the
    remaining elements to the right.

    :note:
        - elements beyond the length of the original array are not written.
        - modify the input array in place, do not return anything from your function.

    :param arr: list of numbers to modify
    :return: None
    """
    index = 0
    length = len(arr)

    while index < length:
        if arr[index] == 0:
            arr.insert(index, 0)
            arr.pop()
            index += 1
        index += 1


def mergeSorted(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

    The number of elements initialized in nums1 and nums2 are m and n respectively. You may assume
    that nums1 has a size equal to m + n such that it has enough space to hold additional
    elements from nums2.

    :param nums1: array to merge into
    :param m: length of nums1
    :param nums2: array to merge from
    :param n: length of nums2
    :return: None
    """
    nums1_copy = nums1[:m]
    p1 = p2 = 0
    for p in range(n+m):
        if p2 > n or (p1 < m and nums1_copy[p1] <= nums2[p2]):
            nums1[p] = nums1_copy[p1]
            p1 += 1
        else:
            nums1[p] = nums2[p2]
            p2 += 1
