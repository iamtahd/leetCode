"""
Leetcode Arrays 101: Deleting Items From an Array
https://leetcode.com/explore/learn/card/fun-with-arrays/526/deleting-items-from-an-array/3246/
"""
from typing import List


def removeElement(nums: List[int], val: int) -> int:
    """"
    Given an array nums and a value val, remove all instances of that value in-place and return
    the new length.

    Do not allocate extra space for another array, you must do this by modifying the input array
    in-place with O(1) extra memory.

    The order of elements can be changed. It doesn't matter what you leave beyond the new length.

    :param nums: nums to delete items from
    :param val: value to remove from nums
    :return: new length of nums after removing values
    """
    i = 0
    while i < len(nums):
        if val == nums[i]:
            nums.pop(i)
        else:
            i += 1
    return len(nums)


def removeDuplicates(nums: List[int]) -> int:
    """
    Given a sorted array nums, remove the duplicates in-place and return
    the new length of the array

    :param nums: array to check
    :return: length of unique values in nums
    """
    if not nums or len(nums) == 0:
        return 0

    j = 1
    for i in range(1, len(nums)):
        if nums[i - 1] != nums[i]:
            nums[j] = nums[i]
            j += 1

    return j
