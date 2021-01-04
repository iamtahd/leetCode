from typing import List
from utils.linkedList import ListNode, LinkedList


def twoSum(nums: List[int], target: int) -> List[int]:
    """
    Given an array of integers, return indices of the two numbers
    such that they add up to a specific target.

    :param List[int] nums: list of candidate values to add
    :param int target: target value

    :return: two integers in nums that add to equal the target
    :rtype: List[int, int]
    """
    cache = dict()
    for i in range(len(nums)):
        if target - nums[i] in cache:
            return [cache[target-nums[i]], i]
        else:
            cache[nums[i]] = i
    return []


def reverse(x: int) -> int:
    """
    Given a 32-bit signed integer, reverse digits of an integer.

    :param int x: int to reverse
    :return: reversed x
    :rtype: int

    :note: Assume we are dealing with an environment which could only store
        integers within the 32-bit signed integer range: [−231,  231 − 1].
        For the purpose of this problem, assume that your function returns
        0 when the reversed integer overflows.
    """
    if x < 0:
        # return with -
        x = abs(x)
        s = str(x)
        s = s[::-1]
        ans = -int(s)
    else:
        s = str(x)
        s = s[::-1]
        ans = int(s)
    if ans < -2147483648 or ans > 2147483647:
        return 0
    else:
        return ans


def isPalindrome(x: int) -> bool:
    """
    Determine whether an integer is a palindrome.

    An integer is a palindrome when it reads the same backward as forward.

    :param int x: int to check

    :return: True if x is a palindrome, False if not
    :rtype: bool
    """
    s = str(x)
    if x < 0:
        return False
    elif x < 10:
        return True
    else:
        for i in range(len(s) // 2 + 1):
            a = s[i]
            b = s[-i-1]
            if a != b:
                return False

    return True


def romanToInt(s: str) -> int:
    """
    Given a roman numeral, convert it to an integer.
    Input is guaranteed to be within the range from 1 to 3999.
    :param str s: roman numeral

    :return: integer corresponding to the roman numeral
    :rtype: int
    """
    d = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    c = {
        'IV': 4,
        'IX': 9,
        'XL': 40,
        'XC': 90,
        'CD': 400,
        'CM': 900
    }
    ans = 0
    for _dict in [c, d]:
        for key, value in _dict.items():
            if key in s:
                ans += value * s.count(key)
                s = s.replace(key, '')
    return ans


def longestCommonPrefix(strs: List[str]) -> str:
    """
    Write a function to find the longest common prefix string amongst
    an array of strings.

    :param List[str] strs:
    :return: common prefix string
    :rtype: str
    """

    letter_groups, longest_pre = zip(*strs), ""
    # print(letter_groups, longest_pre)
    # [('f', 'f', 'f'), ('l', 'l', 'l'), ('o', 'o', 'i'), ('w', 'w', 'g')]
    for letter_group in letter_groups:
        if len(set(letter_group)) > 1:
            break
        longest_pre += letter_group[0]
    return longest_pre


def isValid(s: str) -> bool:
    """
    Given a string containing just the characters:
    '(', ')', '{', '}', '[' and ']',
    determine if the input string is valid.

    An input string is valid if:

        Open brackets must be closed by the same type of brackets.
        Open brackets must be closed in the correct order.

    Note that an empty string is also considered valid.

    :param str s: input string to validate
    :return: True if valid combination of brackets
    """
    mapping = {']': '[', '}': '{', ')': '('}
    stack = []
    for char in s:
        if char in mapping:
            top_element = stack.pop() if stack else '#'
            if mapping[char] != top_element:
                return False
        else:
            stack.append(char)

    return not stack


def mergeTwoListsIterative(l1: ListNode, l2: ListNode) -> ListNode:
    """
    Merge two sorted linked lists and return it as a new list.
    The new list should be made by splicing together the nodes of the
    first two lists.

    :param l1:
    :param l2:

    :return:
    :rtype:
    """
    head = ListNode(-1)
    prev = head

    while l1 and l2:
        if l1.val <= l2.val:
            prev.next = l1
            l1 = l1.next
        else:
            prev.next = l2
            l2 = l2.next
        prev = prev.next
    prev.next = l1 if l1 is not None else l2
    return head.next


def mergeTwoListsRecursive(l1: ListNode, l2: ListNode) -> ListNode:
    """
    Merge two sorted linked lists and return it as a new list.
    The new list should be made by splicing together the nodes of the
    first two lists.

    :param l1:
    :param l2:

    :return:
    :rtype:
    """
    if l1 is None:
        return l2
    elif l2 is None:
        return l1
    elif l1.val <= l2.val:
        l1.next = mergeTwoListsRecursive(l1.next, l2)
        return l1
    else:
        l2.next = mergeTwoListsRecursive(l1, l2.next)
        return l2


def removeDuplicates(nums: List[int]) -> int:
    """
    Given a sorted array nums, remove the duplicates in-place
     such that each element appear only once and return the new length.

    :note: Do not allocate extra space for another array,
        you must do this by modifying the input array in-place
        with O(1) extra memory.

    :param List[int] nums: ordered list of integers

    :return: length of the reduced list
    :rtype: int
    """
    d = 1
    if len(nums) == 0:
        return 0
    for i in range(1, len(nums)):
        if nums[i] != nums[i-1]:
            nums[d] = nums[i]
            d += 1
    return d


def removeElement(nums: List[int], val: int) -> int:
    """
    Given an array nums and a value val, remove all instances of that value
    in-place and return the new length.

    Do not allocate extra space for another array, you must do this
    by modifying the input array in-place with O(1) extra memory.

    The order of elements can be changed. It doesn't matter what you leave
    beyond the new length.

    hint 1:

    :param List[int] nums: list of numbers
    :param int val: value to remove completely from nums
    :return: length of the list with all instances of val removed
    :rtype: int
    """
    r = 0
    c = 0
    for i in range(len(nums)):
        t = i - r
        if nums[t] == val:
            nums.pop(t)
            r += 1
        else:
            c += 1
    return c


def strStr(haystack: str, needle: str) -> int:
    """
    Return the index of the first occurrence of needle in haystack,
     or -1 if needle is not part of haystack.

    Clarification:

    What should we return when needle is an empty string? This is a
    great question to ask during an interview.

    For the purpose of this problem, we will return 0 when needle is
    an empty string.

    :param str haystack: string to search
    :param str needle: substring to find in haystack

    :return: index of the first instance of needle in haystack
    :rtype: int
    """
    if not needle:
        return 0
    elif needle not in haystack:
        return -1
    else:
        return haystack.index(needle)


def searchInsert(nums: List[int], target: int) -> int:
    """
    Given a sorted array and a target value, return the index if the target
    is found. If not, return the index where it would be if it were
    inserted in order.

    You may assume no duplicates in the array.

    :param List[int] nums: sorted list to search for target
    :param int target: term to search for in nums

    :return: index of target in nums or index of where target would
        reside if it were in nums
    :rtype: int
    """
    p, r = 0, len(nums) - 1
    while p <= r:
        z = (p + r) // 2
        if nums[z] == target:
            return z
        elif target < nums[z]:
            r = z - 1
        else:
            p = z + 1
    return p


# todo - look back over this one. PRACTICE REGEX!
def countAndSayRegex(n: int) -> str:
    """

    :param n:
    :return:
    """
    import re
    current = '1'
    pattern = r'((.)\2*)'
    for i in range(n-1):
        nextSeq = []
        for g1, g2 in re.findall(pattern, current):
            nextSeq.append(str(len(g1)))
            nextSeq.append(g2)
        current = ''.join(nextSeq)

    return current


# todo - look back over this one.
def countAndSayRecursion(n: int) -> str:
    """

    :param n:
    :return:
    """
    def nextSequence(m: int, prevSeq):
        if m == 1:
            return prevSeq[:-1]
        nextSeq = []
        prevDigit = prevSeq[0]
        digitCnt = 1
        for digit in prevSeq[1:]:
            if digit == prevDigit:
                digitCnt += 1
            else:
                # the end of a sub-sequence
                nextSeq.extend([str(digitCnt), prevDigit])
                prevDigit = digit
                digitCnt = 1
        # add a delimiter for the next sequence
        nextSeq.append('E')
        return nextSequence(m - 1, nextSeq)

    return ''.join(nextSequence(n, ['1', 'E']))


# todo - look back over this one.
def maxSubArray(nums: List[int]) -> int:
    """
    Given an integer array nums, find the contiguous subarray
    (containing at least one number) which has the largest
    sum and return its sum.

    :param nums: list of integers
    :return: largest sub possible from the subArray
    """
    if not nums:
        return 0
    current_sum = maximum_sum = nums[0]

    for i in range(len(nums)):
        current_sum = max(nums[i], current_sum + nums[i])
        maximum_sum = max(maximum_sum, current_sum)

    return maximum_sum


def reorderLogFiles(logs: List[str]) -> List[str]:
    """
    Reorders a list of logs according to the following rules:

    Rules:
    - Reorder the logs so that all of the letter-logs come before any digit-log.
    - The letter-logs are ordered lexicographically ignoring identifier, with the identifier used in case of ties.
    - The digit-logs should be put in their original order.

    Assumptions:
        It is guaranteed that each log has at least one word after its identifier.
        There are two varieties of logs: letter-logs and digit-logs.

    Return the final order of the logs.
    """

    def filter_(log):
        _id, rest = log.split(" ", 1)
        return (0, rest, _id) if rest[0].isalpha() else (1, )

    return sorted(logs, key=filter_)


def maxProfit(prices: List[int]) -> int:
    buy = float('inf')
    profit = 0

    for i in range(len(prices)):
        if prices[i] < buy:
            buy = prices[i]
        elif prices[i] - buy > profit:
            profit = prices[i] - buy
    return profit


def reverseLinkedList(head: ListNode) -> ListNode:
    prev = None
    curr = head
    while curr is not None:
        nextTemp = curr.next
        curr.next = prev
        prev = curr
        curr = nextTemp
    return prev


def isAlienSorted(words: List[str], order: str) -> bool:
    """
    Asserts whether or not the list of words is sorted according
    to the given 'order' string

    :param words: list of strings to check for sortedness
    :param order: sorting key
    :rtype: bool
    """
    orderIndex = {c: i for i, c in enumerate(order)}

    for i in range(len(words) - 1):
        first = words[i]
        second = words[i + 1]

        for j in range(min(len(first), len(second))):
            if first[j] != second[j]:
                if orderIndex[first[j]] > orderIndex[second[j]]:
                    return False
                break
        else:
            if len(first) > len(second):
                return False
    return True


def addStrings(num1: str, num2: str) -> str:
    return str(int(num1) + int(num2))
