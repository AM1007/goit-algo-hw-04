def quick_sort(arr_):
    arr = arr_[:]
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot] 
    middle = [x for x in arr if x == pivot] 
    right = [x for x in arr if x > pivot] 
    return quick_sort(left) + middle + quick_sort(right)

if __name__ == "__main__":
    numbers = [5, 3, 8, 4, 2]
    print(numbers, quick_sort(numbers))