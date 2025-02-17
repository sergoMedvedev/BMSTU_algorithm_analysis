from turtledemo.penrose import start


def get_array(end, start = 0, step = 1):
    array =[]
    for i in range(start, end, step):
        array.append(i)
    return array

array50v = get_array(500)
array100v = get_array(1000)
array150v = get_array(1500)
array200v = get_array(2000)
array250v = get_array(2500)

array50n = get_array(0, start=500, step=-1)
array100n = get_array(0,start=1000, step=-1)
array150n = get_array(0,start=1500, step=-1)
array200n = get_array(0,start=2000, step=-1)
array250n = get_array(0,start=2500, step=-1)

#массив из позитивных примеров
array_data_v = [
    array50v,
    array100v,
    array150v,
    array200v,
    array250v,
]

array_data_n = [
    array50n,
    array100n,
    array150n,
    array200n,
    array250n,
]

def best_case(n):
    """Генерирует лучший случай для быстрой сортировки (псевдо-сбалансированный массив)"""
    return list(range(1, n + 1))  # Почти сбалансированный массив

def worst_case(n):
    return list(range(n, 0, -1))

# Длина массива

array500Qv = best_case(500)
array1000Qv = best_case(1000)
array1500Qv = best_case(1500)
array2000Qv = best_case(2000)
array2500Qv = best_case(2500)

array_data_q_v = [
    array500Qv,
    array1000Qv,
    array1500Qv,
    array2000Qv,
    array2500Qv
]

array500Qn = worst_case(500)
array1000Qn = worst_case(1000)
array1500Qn = worst_case(1500)
array2000Qn = worst_case(2000)
array2500Qn = worst_case(2500)

array_data_q_n = [
    array500Qn,
    array1000Qn,
    array1500Qn,
    array2000Qn,
    array2500Qn
]


