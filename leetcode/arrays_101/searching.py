"""
Leetcode Arrays 101: Searching For Items In An Array
https://leetcode.com/explore/learn/card/fun-with-arrays/527/searching-for-items-in-an-array/3296/
"""
from typing import List


def checkIfExist(arr: List[int]) -> bool:
    """
    Given an array arr of integers, check if there exists two integers
    N and M such that N is the double of M ( i.e. N = 2 * M).
    """
    d = {}
    for num in arr:
        if num*2 in d or num/2 in d:
            return True
        else:
            d[num] = 0
    return False


def isMountainArray(arr: List[int]) -> bool:
    """
    Given an array of integers, return true iff it is a valid mountain array.

    Mountain Array conditions:
        1. arr.length >= 3
        2. There exists some i with 0 <i < arr.length-1 such that:
            arr[0] < arr[1] < ... arr[i-1] < arr[i]
            arr[i] > arr[i-1] > ... arr[arr.length-1]

    :param arr: array to check
    :return: true if array is mountain array
    """
    n = len(arr)
    i = 0

    # walk up
    while i+1 < n and arr[i] < arr[i+1]:
        i += 1

    # make sure not at start or end of array before walk down
    if i == 0 or i == n-1:
        return False

    # walk down
    while i+1 < n and arr[i] > arr[i+1]:
        i += 1

    # make sure at end of array.
    return i == n-1
