import unittest

from .. import easySet
from utils.linkedList import ListNode, LinkedList


class TestEasySet(unittest.TestCase):
    def assertLinkedListsAreEqual(self, l1: ListNode, l2: ListNode):
        self.assertEqual(l1.val, l2.val)
        if l1.next and l2.next:
            self.assertLinkedListsAreEqual(l1.next, l2.next)

    def testTwoSumCase1(self):
        self.assertEqual([1, 2], easySet.twoSum([3, 2, 4], 6))

    def testReverse(self):
        self.assertEqual(-321, easySet.reverse(-123))
        self.assertEqual(12, easySet.reverse(210))
        self.assertEqual(123, easySet.reverse(321))
        self.assertEqual(0, easySet.reverse(1534236469))

    def testIsPalindrome(self):
        self.assertEqual(True, easySet.isPalindrome(121))
        self.assertEqual(False, easySet.isPalindrome(-121))
        self.assertEqual(True, easySet.isPalindrome(1111))
        self.assertEqual(True, easySet.isPalindrome(11211))
        self.assertEqual(False, easySet.isPalindrome(10))
        self.assertEqual(True, easySet.isPalindrome(0))
        self.assertEqual(False, easySet.isPalindrome(10000021))

    def testRomanToInt(self):
        self.assertEqual(3, easySet.romanToInt('III'))
        self.assertEqual(4, easySet.romanToInt('IV'))
        self.assertEqual(7, easySet.romanToInt('VII'))
        self.assertEqual(9, easySet.romanToInt('IX'))
        self.assertEqual(494, easySet.romanToInt('CDXCIV'))
        self.assertEqual(1494, easySet.romanToInt('MCDXCIV'))
        self.assertEqual(674, easySet.romanToInt('DCLXXIV'))

    def testLongestCommonPrefix(self):
        self.assertEqual('to', easySet.longestCommonPrefix([
            'todd', 'tortuga', 'tomato'
        ]))
        self.assertEqual('', easySet.longestCommonPrefix([
            "dog", "racecar", "car"
        ]))

    def testIsValid(self):
        self.assertEqual(True, easySet.isValid(''), msg='case 1')
        self.assertEqual(True, easySet.isValid('[]'), msg='case 2')
        self.assertEqual(False, easySet.isValid('[(]'), msg='case 3')
        self.assertEqual(False, easySet.isValid('[}'), msg='case 4')
        self.assertEqual(False, easySet.isValid('{[}]'), msg='case 5')
        self.assertEqual(True, easySet.isValid('{}()[]'), msg='case 6')
        self.assertEqual(True, easySet.isValid('{[]}'), msg='case 7')

    def testMergeTwoLists(self):
        self.assertLinkedListsAreEqual(
            LinkedList([1, 2, 2, 3, 3, 4]).head,
            easySet.mergeTwoListsIterative(
                LinkedList([1, 2, 3]).head,
                LinkedList([2, 3, 4]).head)
        )

        self.assertLinkedListsAreEqual(
            LinkedList([1, 2, 2, 3, 3, 4]).head,
            easySet.mergeTwoListsRecursive(
                LinkedList([1, 2, 3]).head,
                LinkedList([2, 3, 4]).head
            )
        )

    def testRemoveDuplicates(self):
        self.assertEqual(3, easySet.removeDuplicates([1, 1, 2, 3]))
        self.assertEqual(1, easySet.removeDuplicates([1, 1, 1, 1]))

    def testRemoveElement(self):
        q1 = ([1, 1, 3], 1)
        a1 = 1
        q2 = ([1, 1, 2], 1)
        a2 = 1
        q3 = ([0, 1, 2, 2, 3, 0, 4, 2], 2)
        a3 = 5
        self.assertEqual(a1, easySet.removeElement(*q1))
        self.assertEqual([3], q1[0][:a1])
        self.assertEqual(a2, easySet.removeElement(*q2))
        self.assertEqual([2], q2[0][:a2])
        self.assertEqual(a3, easySet.removeElement(*q3))
        self.assertEqual([0, 1, 3, 0, 4], q3[0][:a3])

    def testStrStr(self):
        self.assertEqual(2, easySet.strStr('hello', 'll'))
        self.assertEqual(3, easySet.strStr('best test ever', 't'))
        self.assertEqual(-1, easySet.strStr('aaaaa', 'baa'))
        self.assertEqual(0, easySet.strStr('hello', ''))

    def testSearchInsert(self):
        self.assertEqual(2, easySet.searchInsert([1, 3, 5, 6], 5))
        self.assertEqual(1, easySet.searchInsert([1, 3, 5, 6], 2))
        self.assertEqual(4, easySet.searchInsert([1, 3, 5, 6], 7))
        self.assertEqual(0, easySet.searchInsert([1, 3, 5, 6], 0))

    def testCountAndSay(self):
        self.assertEqual('1113213211', easySet.countAndSayRegex(8))
        self.assertEqual('13112221', easySet.countAndSayRegex(7))
        self.assertEqual('312211', easySet.countAndSayRegex(6))

        self.assertEqual('1113213211', easySet.countAndSayRecursion(8))
        self.assertEqual('13112221', easySet.countAndSayRecursion(7))
        self.assertEqual('312211', easySet.countAndSayRecursion(6))

    def testMaxSubArray(self):
        self.assertEqual(
            6,
            easySet.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
        )

    def testReorderLogs(self):
        self.assertEqual(
            easySet.reorderLogFiles(
                [
                    "dig1 8 1 5 1",
                    "let1 art can",
                    "dig2 3 6",
                    "let2 own kit dig",
                    "let3 art zero"
                ]
            ),
            [
                "let1 art can",
                "let3 art zero",
                "let2 own kit dig",
                "dig1 8 1 5 1",
                "dig2 3 6"
            ]
        )

    def testMaxProfit(self):
        self.assertEqual(
            easySet.maxProfit([7, 1, 5, 3, 6, 4]),
            5
        )

    def testReverseLinkedList(self):
        
        self.assertLinkedListsAreEqual(
            easySet.reverseLinkedList(
                LinkedList([1, 2, 3, 4, 5]).head
            ),
            LinkedList([5, 4, 3, 2, 1]).head
        )

    def testIsAlienSorted(self):
        self.assertTrue(
            easySet.isAlienSorted(
                ['hello', 'leetcode'],
                'hlabcdefgijkmnopqrstuvwxyz'
            )
        )
