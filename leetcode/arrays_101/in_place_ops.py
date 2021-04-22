"""
Leetcode Arrays 101: In-Place Operations
https://leetcode.com/explore/learn/card/fun-with-arrays/511/in-place-operations/
"""
from typing import List


def replaceElements(arr: List[int]) -> List[int]:
    """
    Replace every element in the array with the greatest element among the
    elements to its right, and replace the last element with -1.

    :param arr: array of integers to mutate
    :return: mutated array
    """
    n = -1
    for i in range(len(arr)-1, -1, -1):
        tmp = arr[i]
        arr[i] = n
        if tmp > arr[i]:
            n = tmp
    return arr


def moveZeros(nums: List[int]) -> None:
    """
    Given an integer array of nums, move all 0's to the end of it while
    maintaining the relative order of the non-zero elements

    :param nums: array whose zeros should be moved
    :return: None
    """
    pos = 0
    for i, value in enumerate(nums):
        if value != 0:
            nums[pos], nums[i] = nums[i], nums[pos]
            pos += 1


def sortArrayByParity(A: List[int]) -> List[int]:
    """
    Given an array A of non-negative integers, return an array consisting of
    all even elements of A, followed by all the odd elements of A.

    :param A: list to re-arrange in-place
    :return: even members of A followed by odd members of A
    """
    pos = 0
    for i, value in enumerate(A):
        if value % 2 == 0:
            A[pos], A[i] = A[i], A[pos]
            pos += 1

    return A
