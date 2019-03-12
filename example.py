from pyjudge import judge
import random


def test_gen():
    while True:
        total = random.randint(1, 10 ** 7)
        numbers_count = random.randint(1, 10 ** 3)
        numbers = []
        for n in range(numbers_count):
            number = random.randint(1, 10 ** 10)
            numbers.append(number)
        yield (total, numbers)


test_generator = test_gen()

tests = [
    (12, (1, 2, 3, 7, 5)),
    (3, (2, 3, 4, 1, 1, 1)),
    (15, (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)),
    next(test_generator),
    next(test_generator),
    next(test_generator),
]


def brute_force(searched_sum, array):
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            s = sum(array[i : j + 1])
            if s == searched_sum:
                return (i, j)
    return -1


@judge(reference=brute_force, tests=tests)
def solution(searched_sum, array):
    """ Given an unsorted array A of size N of non-negative integers, """
    """ find a continuous sub-array which adds to a given number. """

    total = []
    for a in array:
        if total:
            total += [total[-1] + a]
        else:
            total += [a]
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            s = total[j] - (total[i - 1] if i > 0 else 0)
            if s == searched_sum:
                return (i, j)
    return -1
