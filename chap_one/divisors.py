def find_proper_divisors(number):
    divisors = [1]
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            divisors.append(i)
    return divisors


def find_divisors(number):
    divisors = [1]
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            divisors.append(i)
    divisors.append(number)
    return divisors


def find_divisors0(number):
    divisors = [1]
    for i in range(2, number + 1):
        if number % i == 0:
            divisors.append(i)
    return divisors


if __name__ == '__main__':
    import timeit
    value, value0 = 24, 6
    results = find_proper_divisors(value)
    print(results)
    results0 = find_divisors(value)
    print(results0)
    print(find_divisors0(value))
    print(timeit.timeit('find_divisors(value)', globals=locals(), number=100))
    print(timeit.timeit('find_divisors0(value)', globals=locals(), number=100))
