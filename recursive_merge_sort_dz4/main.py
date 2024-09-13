import time
import random
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    merge_sort(left)
    merge_sort(right)
    
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
    return arr

def test_merge_sort():
    arr = [random.randint(0, 100) for _ in range(10000)]
    merge_sort(arr)
    print(arr)


time_start = time.perf_counter()
test_merge_sort()
time_end = time.perf_counter()
round_time = time_end - time_start
print(f"Time taken: {round_time:.5f} seconds")

    
