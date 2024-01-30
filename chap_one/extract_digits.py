def extract_digits(number):
    remaining_value = number
    while remaining_value > 0:
        digit = remaining_value % 10
        remaining_value = remaining_value // 10
        print(digit, end=' ')
    print()


def extract_digits0(number):
    remaining_value = number
    while remaining_value > 0:
        remaining_value, digit = divmod(remaining_value, 10)
        print(remaining_value, digit)
        print(digit, end=" ")
    print()


def count_digits(number):
    count = 0
    remaining_value = number
    while remaining_value > 0:
        remaining_value, _ = divmod(remaining_value, 10)
        count += 1
    return count


if __name__ == '__main__':
    number = 1233
    extract_digits(number)
    print('switching to next function...')
    extract_digits0(number)
    results = count_digits(number)
    print(results)
