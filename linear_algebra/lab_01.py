# todo - restructure this so that it makes more sense for future labs? maybe just
#   use a test file and a regular file?

# Task 1: Use Python to find the number of minutes in a week.
def minutesInWeek():
    minutes_in_hour = 60
    hours_in_day = 24
    days_per_week = 7
    return minutes_in_hour * hours_in_day * days_per_week


# Task 2: Use Python to find the remainder of 2304811 divided by 47
#   without using the modulo operator %.
def remainder(n, d):
    return n // d


# Task 3: Enter a Boolean expression to test whether the sum of 673 and 909
# is divisible by 3.
def isDivisibleSum(n1, n2, d):
    return (n1 + n2) // d == 0, (n1 + n2) // d


# Task 4: Assign the value -9 to x and 1/2 to y. Predict the value of the following expression, then enter it
# to check your prediction:
# 2**(y+1/2) if x+10<0 else 2**(y-1/2)
def simpleTernary(x, y):
    return 2**(y + 1/2) if x+10 < 0 else 2**(y-1/2)


# Task 5: Write a comprehension over f1; 2; 3; 4; 5g whose value is the set consisting of the squares of the
# first five positive integers.
def squareItems(items):
    return {x**2 for x in items}


# Task 6: Write a comprehension over f0; 1; 2; 3; 4g whose value is the set consisting of the first five powers
# of two, starting with 20.
def expOfBase2(exponents):
    return {2**value for value in exponents}


# Task 7: The value of the previous comprehension,
# fx*y for x in f1,2,3g for y in f2,3,4gg
# is a seven-element set. Replace {1,2,3} and {2,3,4} with two other three-element sets so that the value
# becomes a nine-element set.
def multiplySets(set1, set2):
    return {a*b for a in set1 for b in set2}


# Task 30: Ungraded Task: Write a procedure all 3 digit numbers(base, digits) with the following spec:
# input: a positive integer base and the set digits which should be {0, 1, 2, ... , base - 1g}.
# output: the set of all three-digit numbers where the base is base
def all3DigitNumbers(base):
    # todo
    pass