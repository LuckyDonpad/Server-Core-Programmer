import random
from sorts import *
import timeit
import matplotlib.pyplot as plt


def generate(len: int) -> list:
    test_array = []
    for i in range(len):
        test_array.append(random.randint(0, len))
    return test_array[::]


results = {}
sort_fun = [insertion_sort, heap_sort, quick_sort, merge_sort, bubble_sort, selection_sort, tim_sort]
for foo in sort_fun:
    results[foo.__name__] = {'n_elements': [], 'time': []}

for foo in sort_fun:
    for i in range(100, 3001, 100):
        test_array = generate(i)
        begin = timeit.default_timer()
        if foo is quick_sort or foo is merge_sort:
            foo(test_array, 0, len(test_array) - 1)
        elif foo is selection_sort:
            foo(test_array, len(test_array))
        else:
            foo(test_array)
        end = timeit.default_timer()
        results[foo.__name__]['n_elements'].append(i)
        results[foo.__name__]['time'].append(end - begin)

for foo in sort_fun:
    plt.plot(results[foo.__name__]['n_elements'], results[foo.__name__]['time'], label=foo.__name__)

plt.xlabel('Количество элементов')
plt.ylabel('Время с.')
plt.title('Сравнение быстродействия сортировок')
plt.legend()
plt.show()
