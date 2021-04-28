# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
# from sys import argv
# script_name, hours, hourly_rate, prem = argv
# #print("Имя скрипта: ", script_name)
# print(f'Выработка в часах месяц (ср. 21 день): {hours}')
# print(f'Часовая ставка: {hourly_rate}')
# print(f'Премия: {prem}')
# tmp = (int(hours) * int(hourly_rate)) + int(prem)
# print(f'Зарплата сотрудника в месяц: {tmp - (tmp * 0.13)}')

# 2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
# Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
# Результат: [12, 44, 4, 10, 78, 123].
# from random import randint
# list_num = []
# numb = int(input(f'Введите кол-во элементов в исходном списке: '))
# for i in range(0, numb):
#     list_num.insert(i, randint(0, randint(0, 100)))
# print(f'Исходный список: {list_num}')
#
# total_list = []
# for i in range(0, len(list_num) - 1):
#     if list_num[i+1] > list_num[i]:
#         total_list.append(list_num[i+1])
#         #print(f'Текущее значение: {list_num[i]}, следующее значение: {list_num[i+1]}')
#     else:
#         continue
# print(f'Результирующий список: {total_list}')

# 3. Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Необходимо решить задание в одну строку.
# Подсказка: использовать функцию range() и генератор.
#print([el for el in range(20, 240) if (el % 20 == 0) | (el % 21 == 0)])
#
# 4. Представлен список чисел. Определить элементы списка, не имеющие повторений. Сформировать итоговый массив чисел, соответствующих требованию.
# Элементы вывести в порядке их следования в исходном списке. Для выполнения задания обязательно использовать генератор.
# Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
# Результат: [23, 1, 3, 10, 4, 11]
# from random import randint
# numb = int(input(f'Введите кол-во элементов в исходном списке: '))
# max_number = int(input(f'Введите максимально возможно генерируемое значение элемента списка: '))
# total_list = []
# my_list = [(randint(0, randint(0, max_number))) for el in range(0, numb)]
# print(f'Исходный список: {my_list}')
# for i in my_list:
#     if my_list.count(i) > 1:
#         continue
#     else:
#         total_list.append(i)
# print(f'Итоговый список: {total_list}')
#
# 5. Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().






















#
#
#
# 6. Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools.
# Обратите внимание, что создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
# Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.
#
#
#
# 7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
# При вызове функции должен создаваться объект-генератор.
# Функция должна вызываться следующим образом: for el in fact(n).
# Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.
# Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.