import pytest

from linear_algebra.lab_01 import minutesInWeek
from linear_algebra.lab_01 import remainder
from linear_algebra.lab_01 import isDivisibleSum
from linear_algebra.lab_01 import simpleTernary
from linear_algebra.lab_01 import squareItems
from linear_algebra.lab_01 import expOfBase2
from linear_algebra.lab_01 import multiplySets


def test_minutesInWeek():
    assert minutesInWeek() == 10080


def test_remainder():
    n, d = 2304811, 47
    assert remainder(n, d) == 49038


def test_isDivisibleSum():
    x, y, z = 673, 900, 3
    assert isDivisibleSum(x, y, z)


def test_simpleTernary():
    x, y = -9, 1/2
    assert simpleTernary(x, y) == 1


def test_squareItems():
    assert squareItems({1, 2, 3, 4, 5}) == {1, 4, 9, 16, 25}


def test_expOfBase2():
    assert expOfBase2({0, 1, 2, 3, 4}) == {1, 2, 4, 8, 16}


def test_multiplySets():
    s1, s2 = {1, 2, 3}, {10, 11, 12}
    assert multiplySets(s1, s2) == {33, 36, 10, 11, 12, 20, 22, 24, 30}


def test_multiplySets_nonOverlapping():
    s1, s2 = {1, 2, 3}, {1, 3, 4}
    assert multiplySets(s1, s2) == {1, 2, 3, 4, 6, 8, 9, 12}
