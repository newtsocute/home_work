def karatsuba(x, y, n):
    if n % 2 == 0:
        a = x // (10 ** (n // 2))
        b = x % (10 ** (n // 2))
        c = y // (10 ** (n // 2))
        d = y % (10 ** (n // 2))

        step_4 = (a + b) * (c + d) - (a * c) - (b * d)
        step_5 = (a * c) * (10 ** n) + step_4 * (10 ** (n // 2)) + (b * d)

        return step_5


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
            print(f"Failed: Ожидалось {expected}")


test_karatsuba()