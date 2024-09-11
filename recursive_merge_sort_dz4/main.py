def mergesort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        mergesort(left)
        mergesort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1


def test_func():
    data = [
        [31, 21, 91, 33, 8, 82, 10],
        [5, 7, 6, 6, 1, 3],
        [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    ]

    for i, data in enumerate(data):
        print(f"Тест {i+1}: Входные данные: {data}")
        mergesort(data)
        print(f"Тест {i+1}: Выходны данные: {data}\n")


test_func()
