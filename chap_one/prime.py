def is_prime(number):
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            return False
    return True


if __name__ == '__main__':
    import timeit

    primes = []
    for n in range(2, 100):
        print(timeit.timeit('is_prime(n)', globals=locals()))
        if is_prime(n):
            primes.append(n)
    print(primes)
    print([number for number in range(2, 100) if is_prime(number)])
