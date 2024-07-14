def bubble_sort(lst_):
    lst = lst_.copy()
    n = len(lst)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst

if __name__ == "__main__":
    numbers = [5, 3, 8, 4, 2]
    print(numbers, bubble_sort(numbers))


