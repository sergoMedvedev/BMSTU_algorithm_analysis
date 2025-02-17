import timeit
from alg import bubble_sort, insertion_sort
from data import array_data_v, array_data_n, array_data_q_v, array_data_q_n
import matplotlib.pyplot as plt



print("Лабораторная работа № 1 по вычислительным алгоритмам")
print()
print("""
    (1)         Сортировка пузырьком
    лучший случай это O(n):
      Реализуется, когда массив отсортирован полность и не требует сортировки
    худший случай это O(n^2)
      Реализуется, когда массив необходимо отсортировать от меньшего к большему значению, 
      но массив полность перевернут
      """ ) 

arr_time_v= []
arr_time_n= []
arr_N = [500, 1000, 1500, 2000, 2500]
for arr in array_data_v:
    arr_time_v.append((timeit.timeit(lambda: bubble_sort(arr.copy()), number=10) / 10) * 1000000)


for arr in array_data_n:
    arr_time_n.append((timeit.timeit(lambda: bubble_sort(arr.copy()), number=10) / 10) * 1000)

plt.plot(arr_N, arr_time_v, marker='o', linestyle='-', label="лучший случай (t * 1000)")
plt.plot(arr_N, arr_time_n, marker='o', linestyle='-', label="худший случай")
plt.xlabel("Размер массива (n)")
plt.ylabel("Время выполнения (секунды * 1000)")
plt.title("Зависимость времени пузырьковой сортировки от размера массива")
plt.legend()
plt.grid()
plt.show()


arr_time_v= []
arr_time_n= []
arr_N = [500, 1000, 1500, 2000, 2500]
for arr in array_data_v:
    arr_time_v.append((timeit.timeit(lambda: insertion_sort(arr.copy()), number=10) / 10) * 1000000)


for arr in array_data_n:
    arr_time_n.append((timeit.timeit(lambda: insertion_sort(arr.copy()), number=10) / 10) * 1000)

plt.plot(arr_N, arr_time_v, marker='o', linestyle='-', label="лучший случай (t * 1000)")
plt.plot(arr_N, arr_time_n, marker='o', linestyle='-', label="худший случай")
plt.xlabel("Размер массива (n)")
plt.ylabel("Время выполнения (секунды * 1000)")
plt.title("Зависимость времени сортировки вставкой от размера массива")
plt.legend()
plt.grid()
plt.show()


arr_time_v= []
arr_time_n= []
arr_N = [500, 1000, 1500, 2000, 2500]
for arr in array_data_q_v:
    arr_time_v.append((timeit.timeit(lambda: insertion_sort(arr.copy()), number=10) / 10) * 100000)


for arr in array_data_q_n:
    arr_time_n.append((timeit.timeit(lambda: insertion_sort(arr.copy()), number=10) / 10) * 1000)

plt.plot(arr_N, arr_time_v, marker='o', linestyle='-', label="лучший случай (t * 100)")
plt.plot(arr_N, arr_time_n, marker='o', linestyle='-', label="худший случай")
plt.xlabel("Размер массива (n)")
plt.ylabel("Время выполнения (секунды * 1000)")
plt.title("Зависимость времени быстрой сортировки от размера массива")
plt.legend()
plt.grid()
plt.show()
