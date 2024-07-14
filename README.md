# Sorting algorithms

Python has two built-in sorting functions: `sorted` and `sort`. Python's sorting functions use Timsort, a hybrid sorting algorithm that combines merge sort and insertion sort.

Compare three sorting algorithms: merge sort, insertion sort, and Timsort, in terms of execution time. The analysis should be supported by empirical data obtained by testing the algorithms on various data sets. Empirically verify the theoretical complexity estimates of the algorithms, for example, by sorting large arrays. Use the timeit module to measure the execution time of the algorithms.

Demonstrate that the combination of merge sort and insertion sort makes the Timsort algorithm much more efficient, and this is the reason why programmers, in most cases, use Python's built-in algorithms rather than coding their own. Draw conclusions.

### Аналіз результатів тестування швидкості роботи алгоритмів

На підставі даних вимірювань швидкості роботи різних алгоритмів сортування для невеликих, середніх та великих масивів можна зробити такі висновки:

| Algorithm | Small    | Medium   | Large    |
| --------- | -------- | -------- | -------- |
| Bubble    | 0.000339 | 0.033870 | 4.103813 |
| Insertion | 0.00028  | 0.01462  | 1.86442  |
| Selection | 0.00019  | 0.01696  | 1.87418  |
| Merge     | 0.00017  | 0.00159  | 0.02600  |
| Quick     | 0.00013  | 0.00133  | 0.01774  |
| Radix     | 0.00008  | 0.00085  | 0.01307  |
| Shell     | 0.00006  | 0.00114  | 0.02645  |
| Timsorted | 0.00001  | 0.00008  | 0.00117  |
| Timsort   | 0.00000  | 0.00007  | 0.00102  |

#### Порівняння алгоритмів

**1. Пухирцеве сортування (Bubble Sort)**

- Найповільніший алгоритм у всіх категоріях. На великих масивах час роботи становить понад 20 секунд, що робить його непридатним для використання у реальних завданнях.

**2. Сортування вставками (Insertion Sort) та сортування вибором (Selection Sort)**

- Ці алгоритми показують схожі результати і значно швидше за бульбашкову сортування. Однак, їхній час виконання для великих масивів все ще знаходиться в межах кількох секунд.

**3. Сортування злиттям (Merge Sort)**

- Більш ефективний алгоритм, особливо великих масивів. Час виконання значно менший у порівнянні з попередніми алгоритмами.

**4. Швидке сортування (Quick Sort) та порозрядне сортування (Radix Sort)**

- Ці алгоритми показують ще найкращі результати. Швидке сортування та порозрядне сортування виконуються швидше, ніж сортування злиттям.

**5. Сортування Шелла (Shell Sort)**

- Ефективна для невеликих та середніх масивів, але трохи повільніше на великих масивах у порівнянні з швидким та порозрядним сортуваннями.

**6. Timsort (вбудована в Python функція sorted)**

- Найефективніший алгоритм всім розмірів масивів. Він поєднує в собі переваги сортування злиттям та сортування вставками, що робить його надзвичайно швидким та надійним.

#### Висновок

З даних ясно, що **Timsort** значно перевершує інші алгоритми сортування з ефективності. Завдяки використанню комбінації сортування злиттям та сортування вставками **Timsort** оптимізує роботу на різних масивах даних, забезпечуючи швидке виконання навіть для великих масивів.

З цієї причини програмісти часто вважають за краще використовувати вбудовані в Python функції сортування, такі як `sorted` і `sort` замість написання власних алгоритмів сортування. Вбудовані функції забезпечують високу продуктивність, перевірені на надійність та оптимізовані для різних сценаріїв використання.
