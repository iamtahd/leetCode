"""
Test suite for  Conclusions & What's Next
https://leetcode.com/explore/learn/card/fun-with-arrays/523/conclusion/3220/
"""
from leetcode.arrays_101.conclusions import heightChecker
from leetcode.arrays_101.conclusions import findMaxConsecutiveOnesII
from leetcode.arrays_101.conclusions import findDisappearingNumbers
from leetcode.arrays_101.conclusions import findThirdMaximumNumber


def testHeightChecker():
    assert heightChecker([1, 1, 4, 2, 1, 3]) == 3
    assert heightChecker([5, 1, 2, 3, 4]) == 5
    assert heightChecker([1, 2, 3, 4, 5]) == 0


def testFindMaxConsecutiveOnesII():
    assert findMaxConsecutiveOnesII([1, 0, 1, 1, 0]) == 4
    assert findMaxConsecutiveOnesII([1, 0, 1, 1, 0, 1, 1, 0, 0, 1]) == 5


def testFindThirdMaximumNumber():
    assert findThirdMaximumNumber([2, 2, 3, 1]) == 1
    assert findThirdMaximumNumber([2, 2, 3, 1, -4, -5, -99, 0, 100]) == 2


def testFindDisappearedNumbers():
    assert findDisappearingNumbers([4, 3, 2, 7, 8, 2, 3, 1]) == [5, 6]
    assert findDisappearingNumbers([1, 1]) == [2]
