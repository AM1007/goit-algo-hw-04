def selection_sort(arr_):
    arr = arr_[:]
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx =j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

if __name__ == "__main__":
    numbers = [5, 3, 8, 4, 2]
    print(numbers, selection_sort(numbers))

