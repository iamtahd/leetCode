import unittest

from ..challenges import GoogleChallenges


class TestEasySet(unittest.TestCase):
    def testSolution1(self):
        self.assertEqual(
            [],
            GoogleChallenges.challengeSolution1([1, 2, 3], 0)
        )
        self.assertEqual(
            [1, 4],
            GoogleChallenges.challengeSolution1([1, 2, 2, 3, 3, 3, 4, 5, 5], 1)
        )
        self.assertEqual(
            [5, 15, 7],
            GoogleChallenges.challengeSolution1(
                [5, 10, 15, 10, 7],
                1
            )
        )
        self.assertEqual(
            [1, 2, 3],
            GoogleChallenges.challengeSolution1(
                [1, 5, 5, 5, 2, 5, 5, 5, 5, 3],
                5
            )
        )
