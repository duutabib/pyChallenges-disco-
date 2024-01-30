from typing import List, Any

from prime import is_prime


def calc(m: int, n: int):
    _, r = divmod((m * n) // 2, 7)
    return r


def test_calc():
    assert calc(6, 7) == 0
    assert calc(5, 5) == 5
    return True


def cal_sum_and_count_all_div_by_2_or_7(n: int) -> (int, int):
    counter = 0
    sum0 = 0
    for num in range(1, n):
        if (num % 2 == 0) or (num % 7 == 0):
            counter += 1
            sum0 += num
    return counter, sum0


def test_sum_and_count_all_div_by_2_or_7():
    assert cal_sum_and_count_all_div_by_2_or_7(3) == (1, 2)
    assert cal_sum_and_count_all_div_by_2_or_7(8) == (4, 19)
    assert cal_sum_and_count_all_div_by_2_or_7(15) == (8, 63)
    print(True)


def is_even(n: int) -> bool:
    return True if n % 2 == 0 else False


def is_odd(n: int) -> bool:
    return True if n % 2 == 1 else False


def test_is_even() -> None:
    raise "Not implemented "


# this implementation is incorrect.
def number_as_text(n: int) -> str:
    remainder = n % 10
    value_to_text = ""
    if remainder == 0:
        value_to_text = 'ZER0'
    if remainder == 1:
        value_to_text = "ONE"
    if remainder == 2:
        value_to_text = "TWO"
    if remainder == 3:
        value_to_text = "THREE"
    if remainder == 4:
        value_to_text = "FOUR"
    if remainder == 5:
        value_to_text = "FIVE"
    if remainder == 6:
        value_to_text = "SIX"
    if remainder == 7:
        value_to_text = "SEVEN"
    if remainder == 8:
        value_to_text = "EIGHT"
    if remainder == 9:
        value_to_text = "NINE"
    return value_to_text


# def divisors for n
# verify function

def get_divisors(n: int) -> list[int | Any]:
    list_of_divisors = [1]
    for j in range(2, n):
        if n % j == 0:
            list_of_divisors.append(j)
    return list_of_divisors


def is_perfect_number(n: int) -> bool:
    if n == sum(get_divisors(n)):
        return True


def get_perfect_numbers(n) -> list[int: Any]:
    list_of_perfect_numbers = []
    for num in range(n):
        if is_perfect_number(num):
            list_of_perfect_numbers.append(num)
    return list_of_perfect_numbers


def calc_primes_up_to(max_value: int) -> list[int]:
    list_of_primes = []
    for num in range(max_value):
        if is_perfect_number(num):
            list_of_primes.append(num)
    return list_of_primes


def twin_primes(n) -> bool:
    if is_prime(n) & is_prime(n+2):
        return True


def cousin_primes(n) -> bool:
    if is_prime(n) & is_prime(n+4):
        return True


def sexy_primes(n) -> bool:
    if is_prime(n) & is_prime(n+6):
        return True


if __name__ == '__main__':
    print(number_as_text(111))

