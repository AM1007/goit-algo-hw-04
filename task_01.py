import timeit
import random

# Merge Sort
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Test arrays
sizes = [1000, 10000, 100000]
arrays = {size: [random.randint(0, 10000) for _ in range(size)] for size in sizes}

# Time measurement
for size in sizes:
    arr = arrays[size]
    
    print(f"Array size: {size}")

    # Time for merge sort
    time_merge_sort = timeit.timeit(lambda: merge_sort(arr.copy()), number=1)
    print(f"Merge Sort: {time_merge_sort:.6f} seconds")

    # Time for insertion sort
    time_insertion_sort = timeit.timeit(lambda: insertion_sort(arr.copy()), number=1)
    print(f"Insertion Sort: {time_insertion_sort:.6f} seconds")

    # Time for Timsort (Python's built-in sort)
    time_timsort = timeit.timeit(lambda: sorted(arr.copy()), number=1)
    print(f"Timsort (sorted): {time_timsort:.6f} seconds")

    print()
