"""
Leetcode Arrays 101: Accessing Arrays
https://leetcode.com/explore/learn/card/fun-with-arrays/521/introduction/3238/
"""
from typing import List


def findMaxConsecutiveOnes(nums: List[int]) -> int:
    """
    Return the maximum count of consecutive values where the value == 1

    :param nums: array to inspect
    :return: maximum consecutive value count
    """
    count = maxCount = 0
    for num in nums:
        if num == 1:
            count += 1
        else:
            maxCount = max([count, maxCount])
            count = 0
    return max([count, maxCount])


def findNumbers(nums: List[int]) -> int:
    """
    Given an array nums of integers, return how many of them contain an even number of digits.

    :param nums: list of integers to interrogate for even lengths of digits
    :return: members of nums with an even length
    """
    even = 0
    for num in nums:
        temp = str(num)
        if len(temp) % 2 == 0:
            even += 1
    return even


def sortedSquares(nums: List[int]) -> List[int]:
    """
    Given an integer array nums sorted in non-decreasing order, return an array of
    the squares of each number sorted in non-decreasing order.

    :param nums: integers to square and re-sort
    :return: squared and sorted nums
    """
    return sorted([n*n for n in nums])
