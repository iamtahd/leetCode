"""
Leetcode Arrays 101: Conclusions & What's Next
https://leetcode.com/explore/learn/card/fun-with-arrays/523/conclusion/3220/
"""
from typing import List


def heightChecker(heights: List[int]) -> int:
    """
    Check given heights against expected ordering, return mismatches.

    A school is trying to take an annual photo of all the students. The students
    are asked to stand in a single file line in non-decreasing order by height.
    Let this ordering be represented by the integer array "expected" where
    "expected[i]" is the expected height of the i-th student in line.

    Constraints:
        - 1 <= heights.length <= 100
        - 1 <= heights[i] <= 100

    :param heights: current order that the students are standing in.
    :return: number of heights[i] != expected[i]
    """
    expected = sorted(heights)
    mismatched = 0
    for expected, actual in zip(expected, heights):
        if expected != actual:
            mismatched += 1
    return mismatched


def findMaxConsecutiveOnesII(nums: List[int]) -> int:
    """
    Given a binary array nums, return the maximum number of
    consecutive 1's in the array if you can flip at most one 0.

    :param nums: array to inspect
    :return: maximum consecutive value count
    """
    count = maxCount = current = 0
    for num in nums:
        count += 1
        if num == 0:
            current = count
            count = 0
        maxCount = max([maxCount, count + current])

    return maxCount


def findThirdMaximumNumber(nums: List[int]) -> int:
    """
    Given integer array nums, return the third maximum number in this array. If
    the third maximum does not exist, return the maximum number.

    :param nums: integers to interrogate
    :return: third maximum num | maximum num
    """

    if len(set(nums)) < 3:
        return max(nums)
    else:
        return sorted(list(set(nums)))[-3]


def findDisappearingNumbers(nums: List[int]) -> List[int]:
    """
    Given an array nums of n integers where nums[i] is in the range [1, n], return
    an array of all the integers in the range [1, n] that do not appear in nums.

    :param nums:
    :return: list of ints that are not included in the range
    """
    return list(set(list(range(1, len(nums)+1))) - set(nums))
