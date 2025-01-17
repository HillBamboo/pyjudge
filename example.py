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
    (5, (1, 2, 3, 7, 5)),
    (12, (1, 2, 3, 7, 5)),
    (3, (2, 3, 4, 1, 1, 1)),
    (15, (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)),
    (23, (1, 1, 1, 1, 2, 3, 1, 1, 3, 23)),
    next(test_generator),
    next(test_generator),
    next(test_generator),
]


def brute_force(searched_sum, array):
    for i in range(len(array)):
        for j in range(i, len(array)):
            s = sum(array[i : j + 1])
            if s == searched_sum:
                return (i, j)
    return -1


@judge(reference_solution=brute_force, tests=tests)
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
        for j in range(i, len(array)):
            s = total[j] - (total[i - 1] if i > 0 else 0)
            if s == searched_sum:
                return (i, j)
    return -1


@judge(reference_solution=brute_force, tests=tests)
def solution2(subsequent_sum, array):
    # i, j = 0, 0
    # total = array[0]
    # while total != subsequent_sum and i <= j and j < len(array):
    #     if total < subsequent_sum:
    #         j += 1
    #         if j < len(array):
    #             total += array[j]
    #     else:
    #         if i == j:
    #             return -1
    #         total -= array[i]
    #         i += 1
    # if total == subsequent_sum:
    #     return (i, j)
    # else:
    #     return -1
    return -1

# for data in tests:
#     solution2(*data)