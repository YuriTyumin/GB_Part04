# 1. Поработайте с переменными, создайте несколько, выведите на экран,
# запросите у пользователя несколько чисел и строк и сохраните в переменные,
# выведите на экран.
# n = 0
# list = []
# counter = int(input(f'Введите кол-во переменных: '))
# while n <= counter - 1:
#     var = input(f'Введите значение {n + 1} переменной: ')
#     print(f'{n + 1} переменная: {var}')
#     list.insert(n, var)
#     # print(list[n])
#     n += 1

# 2. Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.
# time_counter = int(input(f'Введите кол-во секунд: '))
# hour = time_counter // 3600
# min = (time_counter % 3600) // 60
# sec = time_counter % 60
# print(f'{hour}:{min}:{sec}')

# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369
# number = input(f'Введите число от 1 до 9: ')
# num2 = (number * 2)
# #print(num2)
# num3 = (number * 3)
# #print(num3)
# print(f'Сумма {number} + {num2} + {num3} = {int(number) + int(num2) + int(num3)}')

# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.
# counter_input = input(f'Введите целое положительное число: ')
# length = len(counter_input)
# biggest = counter_input[0]
# counter_array = 0
# while length > int(counter_array):
#     if int(counter_input[counter_array]) > int(biggest):
#         biggest = counter_input[counter_array]
#         counter_array +=1
#     else:
#         counter_array +=1
#         continue
# print(f'Наибольшая цифра: {biggest}')