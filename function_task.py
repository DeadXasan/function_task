# Задача 1:  Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
#            Каждое число вводится с новой строки.

# Ввод первого элемента, разности и количества элементов
a1 = int(input("Введите первый элемент (a1): "))
d = int(input("Введите разность (d): "))
n = int(input("Введите количество элементов (n): "))

# Инициализация пустого массива для хранения элементов
arithmetic_progression = []

# Вычисление и добавление каждого элемента в массив
for i in range(n):
    element = a1 + i * d
    arithmetic_progression.append(element)

# Вывод массива
print("Арифметическая прогрессия:")
for element in arithmetic_progression:
    print(element)

# --------------------------------------------------------------------------------------------------------------

# Задача 2: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)

# Функция для поиска индексов элементов в заданном диапазоне
def find_indices_in_range(arr, min_value, max_value):
    indices = []
    for i in range(len(arr)):
        if min_value <= arr[i] <= max_value:
            indices.append(i)
    return indices

# Пример списка
my_list = [10, 5, 15, 8, 20, 25, 3]

# Заданный диапазон
min_value = 5
max_value = 15

# Находим индексы элементов в заданном диапазоне
result_indices = find_indices_in_range(my_list, min_value, max_value)

# Выводим результат на экран
if result_indices:
    print(f"Индексы элементов в диапазоне от {min_value} до {max_value}: {result_indices}")
else:
    print("В заданном диапазоне нет элементов.")