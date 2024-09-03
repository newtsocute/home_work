def karatsuba(x, y, n):
    if n == 1 or x < 10 or y < 10: #просто проверка если длина числа меньше либо равно одному то перемножаем
        return x * y

    m = n // 2
    a = x // (10 ** m)
    b = x % (10 ** m)
    c = y // (10 ** m)
    d = y % (10 ** m)

    ac = karatsuba(a, c, m)
    bd = karatsuba(b, d, m)
    ad_plus_bc = karatsuba(a + b, c + d, m + 1) - ac - bd

    result = ac * (10 ** (2 * m)) + ad_plus_bc * (10 ** m) + bd

    return result


def test_karatsuba():
    enter_numbers = [
        [567812, 123412, 6],
        [511686, 586319, 6],
        [12345, 98765, 5],
    ]

    expected_results = [
        70074814544,
        300011223834,
        1219253925
    ]

    for i in range(len(enter_numbers)):
        x, y, n = enter_numbers[i]
        expected = expected_results[i]
        result = karatsuba(x, y, n)

        print(f"Test {i + 1}")
        if result == expected:
            print(f"Complete: {result}")
        else:
            print(f"Failed: Ожидалось {expected}, получено {result}")


test_karatsuba()
