# Sorting algorithms

Python has two built-in sorting functions: `sorted` and `sort`. Python's sorting functions use Timsort, a hybrid sorting algorithm that combines merge sort and insertion sort.

Compare three sorting algorithms: merge sort, insertion sort, and Timsort, in terms of execution time. The analysis should be supported by empirical data obtained by testing the algorithms on various data sets. Empirically verify the theoretical complexity estimates of the algorithms, for example, by sorting large arrays. Use the timeit module to measure the execution time of the algorithms.

Demonstrate that the combination of merge sort and insertion sort makes the Timsort algorithm much more efficient, and this is the reason why programmers, in most cases, use Python's built-in algorithms rather than coding their own. Draw conclusions.

Optional Task

Given `𝑘` sorted lists of integers, your task is to merge them into one sorted list. You can rely on the merge sort algorithm from the lecture notes. Implement the `merge_k_lists` function, which takes a list of sorted lists as input and returns a sorted list.

Expected result example:

```python
lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged_list = merge_k_lists(lists)
print("Sorted list:", merged_list)
```

Output:

```python
Sorted list: [1, 1, 2, 3, 4, 4, 5, 6]
```
