

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
    return {2**exp for exp in exponents}


# Task 7: The value of the previous comprehension,
# fx*y for x in f1,2,3g for y in f2,3,4gg
# is a seven-element set. Replace {1,2,3} and {2,3,4} with two other three-element sets so that the value
# becomes a nine-element set.
def multiplySets(set1, set2):
    return {a*b for a in set1 for b in set2}


if __name__ == "__main__":

    # Task 1
    print(f'Task1: minutes in a week: {minutesInWeek()}')

    # Task 2
    x, y = 2304811, 47
    print(f'Task2: remainder of {x} / {y} without using "%": {remainder(x, y)}')

    # Task 3
    x, y, z = 673, 900, 3
    print(f'Task3: sum {x} + {y}, divisible by {z}: {isDivisibleSum(x, y, z)}')

    # Task 4
    # todo - clean up ?
    print(f'Task4: check ternary: {simpleTernary(-9, 1/2)}')

    # Task 5
    s = {1, 2, 3, 4, 5}
    print(f'Task5: square the set: {s} -> {squareItems(s)}')

    # Task 6
    exp = {0, 1, 2, 3, 4}
    print(f'Task6: 2 raised to set of exponents: {exp} -> {expOfBase2(exp)}')

    # Task 7
    s1, s2 = {1, 2, 3}, {10, 11, 12}
    print(f'Task7: multiplied union of sets {s1}, {s2} -> '
          f'{multiplySets(s1, s2)}')

    # Task 8
    s1, s2 = {1, 2, 3}, {10, 11, 12}
    print(f'Task8: multiply non-overlapping sets: {s1}, {s2} ->'
          f' {multiplySets(s1, s2)}')

    z = 1