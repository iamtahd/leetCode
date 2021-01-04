from utils.linkedList import LinkedList, ListNode

from .. import easy


def assertLinkedListsAreEqual(l1: ListNode, l2: ListNode):
    assert l1.val == l2.val
    if l1.next and l2.next:
        assertLinkedListsAreEqual(l1.next, l2.next)


def testTwoSumCase1():
    assert [1, 2] == easy.twoSum([3, 2, 4], 6)


def testReverse():
    assert -321 == easy.reverse(-123)
    assert 12 == easy.reverse(210)
    assert 123 == easy.reverse(321)
    assert 0 == easy.reverse(1534236469)


def testIsPalindrome():
    assert easy.isPalindrome(121)
    assert not easy.isPalindrome(-121)
    assert easy.isPalindrome(1111)
    assert easy.isPalindrome(11211)
    assert not easy.isPalindrome(10)
    assert easy.isPalindrome(0)
    assert not easy.isPalindrome(10000021)


def testRomanToInt():
    assert 3 == easy.romanToInt("III")
    assert 4 == easy.romanToInt("IV")
    assert 7 == easy.romanToInt("VII")
    assert 9 == easy.romanToInt("IX")

    # noinspection SpellCheckingInspection
    assert 494 == easy.romanToInt("CDXCIV")

    # noinspection SpellCheckingInspection
    assert 1494 == easy.romanToInt("MCDXCIV")

    # noinspection SpellCheckingInspection
    assert 674 == easy.romanToInt("DCLXXIV")


def testLongestCommonPrefix():
    assert "to" == easy.longestCommonPrefix(["todd", "tortuga", "tomato"])
    assert "" == easy.longestCommonPrefix(["dog", "racecar", "car"])


def testIsValid():
    assert easy.isValid("")
    assert easy.isValid("[]")
    assert not easy.isValid("[(]")
    assert not easy.isValid("[}")
    assert not easy.isValid("{[}]")
    assert easy.isValid("{}()[]")
    assert easy.isValid("{[]}")


def testMergeTwoLists():
    assertLinkedListsAreEqual(
        LinkedList([1, 2, 2, 3, 3, 4]).head,
        easy.mergeTwoListsIterative(
            LinkedList([1, 2, 3]).head, LinkedList([2, 3, 4]).head
        ),
    )

    assertLinkedListsAreEqual(
        LinkedList([1, 2, 2, 3, 3, 4]).head,
        easy.mergeTwoListsRecursive(
            LinkedList([1, 2, 3]).head, LinkedList([2, 3, 4]).head
        ),
    )


def testRemoveDuplicates():
    assert 3 == easy.removeDuplicates([1, 1, 2, 3])
    assert 1 == easy.removeDuplicates([1, 1, 1, 1])


def testRemoveElement():
    q1 = ([1, 1, 3], 1)
    a1 = 1
    q2 = ([1, 1, 2], 1)
    a2 = 1
    q3 = ([0, 1, 2, 2, 3, 0, 4, 2], 2)
    a3 = 5
    assert a1 == easy.removeElement(*q1)
    assert [3] == q1[0][:a1]
    assert a2 == easy.removeElement(*q2)
    assert [2] == q2[0][:a2]
    assert a3 == easy.removeElement(*q3)
    assert [0, 1, 3, 0, 4] == q3[0][:a3]


def testStrStr():
    assert 2 == easy.strStr("hello", "ll")
    assert 3 == easy.strStr("best test ever", "t")

    # noinspection SpellCheckingInspection
    assert -1 == easy.strStr("aaaaa", "baa")
    assert 0 == easy.strStr("hello", "")


def testSearchInsert():
    assert 2 == easy.searchInsert([1, 3, 5, 6], 5)
    assert 1 == easy.searchInsert([1, 3, 5, 6], 2)
    assert 4 == easy.searchInsert([1, 3, 5, 6], 7)
    assert 0 == easy.searchInsert([1, 3, 5, 6], 0)


def testCountAndSay():
    assert "1113213211" == easy.countAndSayRegex(8)
    assert "13112221" == easy.countAndSayRegex(7)
    assert "312211" == easy.countAndSayRegex(6)

    assert "1113213211" == easy.countAndSayRecursion(8)
    assert "13112221" == easy.countAndSayRecursion(7)
    assert "312211" == easy.countAndSayRecursion(6)


def testMaxSubArray():
    assert 6 == easy.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])


def testReorderLogs():
    assert easy.reorderLogFiles(
        [
            "dig1 8 1 5 1",
            "let1 art can",
            "dig2 3 6",
            "let2 own kit dig",
            "let3 art zero",
        ]
    ) == [
        "let1 art can",
        "let3 art zero",
        "let2 own kit dig",
        "dig1 8 1 5 1",
        "dig2 3 6",
    ]


def testMaxProfit():
    assert easy.maxProfit([7, 1, 5, 3, 6, 4]) == 5


def testReverseLinkedList():
    assertLinkedListsAreEqual(
        easy.reverseLinkedList(LinkedList([1, 2, 3, 4, 5]).head),
        LinkedList([5, 4, 3, 2, 1]).head,
    )


def testIsAlienSorted():
    assert easy.isAlienSorted(["hello", "leetcode"], "hlabcdefgijkmnopqrstuvwxyz")

    # noinspection SpellCheckingInspection
    assert not easy.isAlienSorted(
        ["word", "world", "row"], order="worldabcefghijkmnpqstuvxyz"
    )

    # noinspection SpellCheckingInspection
    assert not easy.isAlienSorted(["apple", "app"], "abcdefghijklmnopqrstuvwxyz")

    # noinspection SpellCheckingInspection
    assert easy.isAlienSorted(["kuvp", "q"], "ngxlkthsjuoqcpavbfdermiywz")


def testAddStrings():
    assert easy.addStrings("3", "4") == "7"
