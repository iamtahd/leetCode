from typing import List


# ------------- ACCESSING ARRAYS -------------
def findMaxConsecutiveOnes(nums: List[int]) -> int:
    count = maxCount = 0
    for num in nums:
        if num == 1:
            count += 1
        else:
            maxCount = max([count, maxCount])
            count = 0
    return max([count, maxCount])


def findNumbers(nums: List[int]) -> int:
    even = 0
    for num in nums:
        temp = str(num)
        if len(temp) % 2 == 0:
            even += 1
    return even


def sortedSquares(nums: List[int]) -> List[int]:
    return sorted([n*n for n in nums])


# ------------- INSERTING ITEMS INTO ARRAYS -------------
def duplicateZeros(arr: List[int]) -> None:
    duplicates = 0
    length = len(arr) - 1

    for left in range(length+1):
        if left > length - duplicates:
            break
        if arr[left] == 0:
            if left == length - duplicates:
                arr[length] = 0
                length -= 1
                break
            duplicates += 1

    last = length - duplicates
    for i in range(last, -1, -1):
        if arr[i] == 0:
            arr[i + duplicates] = 0
            duplicates -= 1
            arr[i + duplicates] = 0
        else:
            arr[i + duplicates] = arr[i]


def duplicateZerosClever(arr: List[int]) -> None:
    n_zer = arr.count(0)
    l = len(arr)
    for i in range(l-1, -1, -1):
        if n_zer + i < l:
            arr[n_zer + i] = arr[i]
        if arr[i] == 0:
            n_zer -= 1
            if n_zer + i < l:
                arr[n_zer + i] = 0


def duplicateZerosSimple(arr: List[int]) -> None:
    index = 0
    length = len(arr)

    while index < length:
        if arr[index] == 0:
            arr.insert(index, 0)
            arr.pop()
            index += 1
        index += 1


def mergeSorted(nums1, m, nums2, n) -> None:
    # O((n+m)log(n+m)) - not the best, but simple.
    for i in range(n):
        nums1[i+m] = nums2[i]
    nums1.sort()


def mergeSortedOptimized(nums1, m, nums2, n) -> None:
    nums1_copy = nums1[:m]
    p1 = p2 = 0
    for p in range(n+m):
        if p2 > n or (p1 < m and nums1_copy[p1] <= nums2[p2]):
            nums1[p] = nums1_copy[p1]
            p1 += 1
        else:
            nums1[p] = nums2[p2]
            p2 += 1


# ------------- DELETING ITEMS FROM ARRAYS -------------
def removeElement(nums: List[int], val: int) -> int:
    count = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[count] = nums[i]
            count += 1
    return count


def removeElementWhile(nums: List[int], val: int) -> int:
    i = 0
    while i < len(nums):
        if val == nums[i]:
            nums.pop(i)
        else:
            i += 1
    return len(nums)


def removeDuplicates(nums: List[int]) -> int:
    if not nums or len(nums) == 0:
        return 0

    j = 1
    for i in range(1, len(nums)):
        if nums[i - 1] != nums[i]:
            nums[j] = nums[i]
            j += 1

    return j


# ------------- SEARCHING ARRAYS -------------
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


# Mine
def myIsMountainArray(arr: List[int]) -> bool:

    arrLen = len(arr)
    if arrLen < 3:
        return False

    maxIndex = arr.index(max(arr))
    if maxIndex == arrLen-1 or maxIndex == 0:
        return False

    for i in range(1, arrLen):
        diff = arr[i] - arr[i-1]
        if diff == 0:
            return False
        if diff > 0 and i > maxIndex:
            return False
        if diff < 0 and i < maxIndex:
            return False

    return True


# Better Solution
def isMountainArray(arr: List[int]) -> bool:
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


# ------------- IN-PLACE OPERATIONS WITH ARRAYS -------------
def replaceElements(arr: List[int]) -> List[int]:
    # crushed it on this one!
    n = -1
    for i in range(len(arr)-1, -1, -1):
        tmp = arr[i]
        arr[i] = n
        if tmp > arr[i]:
            n = tmp
    return arr

