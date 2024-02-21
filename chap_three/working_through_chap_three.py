import functools


def factorial(n):
    if n < 0:
        raise ValueError("n must be positive integer")
    # recursion termination
    if n == 0 or n == 1:
        return 1
    # recursive descent
    return n*factorial(n-1)


def factorial0(n):
    return functools.reduce(lambda n_1, n: n_1*n, range(1, n+1))


def sum_of(n):
    if n < 0:
        raise ValueError("n must be positive integer")
    if n == 1:
        return 1
    return n + sum_of(n-1)


def sum_of0(n):
    return functools.reduce(lambda n_1, n: n_1+n, range(1, n+1))
