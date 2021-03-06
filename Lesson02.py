# 1. Создать список и заполнить его элементами различных типов данных. Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа. Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
list = [int(2),
        str('te2350xt'),
        tuple('23r'),
        float(45.3),
        None,
        set('flkgm678nfkgn'),
        frozenset('dfngdk938fgnkdfj'),
        dict(name='Mike', age=None),
        bytes('fk45mbfg', 'UTF-8'),
        bytearray('lfg23kmngf', 'UTF-8')]
for pos in list:
    print(f'Элемент {pos} имеет тип: {type(pos)}')

# 2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте. Для заполнения списка элементов необходимо использовать функцию input().
n = 0
list = []
counter = int(input(f'Введите кол-во элементов списка: '))
while n <= counter - 1:
    var = input(f'Введите значение элемента {n + 1}: ')
    list.insert(n, var)
    n += 1
print(f'Список до изменения:')
print(list)
n = 0
while n + 1 < counter:
    tmp1 = list[n]
    tmp2 = list[n + 1]
    list[n] = tmp2
    list[n + 1] = tmp1
    n += 2
print(f'Список после изменения:')
print(list)

# 3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.
month = int(input(f'Введите месяц года в числовом виде: '))
month_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
month_dict = {'зима': (1, 2, 12), 'весна': (3, 4, 5), 'лето': (6, 7, 8), 'осень': (9, 10, 11)}
index_list = month_list.index(month)
print(f'Позиция в {month_list}: {index_list}')
if 2 <= index_list <= 5:
    print(f'Месяц относится к весне')
elif 5 <= index_list <= 7:
    print(f'Месяц относится к лету')
elif 7 <= index_list <= 9:
    print(f'Месяц относится к осени')
else:
    print(f'Месяц относится к зиме')
for el in month_dict:
    tmp_tuple = list(month_dict.get(el))
    try:
        if 0 <= tmp_tuple.index(month) <= 3:
            print(f'Время года данного месяца: {el}')
            break
        else:
            continue
    except ValueError:
        continue

# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки.
# Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.
string = input(f'Введите строку из нескольких слов, разделенных пробелами: ')
n = 1
for el in string.split():
    if len(el) < 10:
        print(f'{n}: {el}')
    else:
        print(f'{n}: {el[0:10]}')
    n += 1

# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].
# string = input(f'Введите элементы рейтинга в виде целых положительных чисел, разделенных пробелами: ')
# splited_list = string.split()
# print(f'Список до сортировки: {splited_list}')
# splited_list.sort()
# splited_list.reverse()
# print(f'Список после сортровки: {splited_list}')
splited_list = [12, 12, 10, 6, 6, 4]
var = int(input(f'Введите новый элемент рейтинга: '))
# print(splited_list.count(var))
for ind, el in enumerate(splited_list):
    print(f'{ind}: {el}')
    if var <= el:
        if ind == len(splited_list) - 1:
            splited_list.append(var)
            print(f'Результат: {splited_list})
            break
        continue
    else:
        splited_list.insert(ind, var)
        print(f'Результат: {splited_list})
        break

# 6. *Реализовать структуру данных «Товары». Она должна представлять собой список кортежей. Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
#
# Пример готовой структуры:
#
# [
#     (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
#     (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
#     (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]
#
# Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара, например название, а значение — список значений-характеристик, например список названий товаров.
#
# Пример:
#
# {
# “название”: [“компьютер”, “принтер”, “сканер”],
# “цена”: [20000, 6000, 2000],
# “количество”: [5, 2, 7],
# “ед”: [“шт.”]
# }