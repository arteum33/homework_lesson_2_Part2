#Задачи на циклы и оператор условия------
#----------------------------------------

'''
# Задача 1
# Вывести на экран циклом пять строк из нулей, причем каждая строка должна быть пронумерована.
a = 0
for i in range(5):
    print(i+1, a, sep='.')
'''


'''
# Задача 2
# Пользователь в цикле вводит 10 цифр. Найти количество введеных пользователем цифр 5.
i = 0
count = 0
while i < 10:
    number = input('введите число от 1 до 10: ')
    number = int(number)
    if number == 5:
        count = count + 1
    i = i + 1
    if i == 10: break
print('Количество повторов числа 5: ', count)
'''


'''
# Задача 3
# Найти сумму ряда чисел от 1 до 100. Полученный результат вывести на экран.

sum = 0
for i in range(1,101):
    sum += i
print(sum)
'''


'''
# Задача 4
# Найти произведение ряда чисел от 1 до 10. Полученный результат вывести на экран.

multiplication = 1
for i in range(1,10):
    multiplication *= i
print(multiplication)
'''

'''
# Задача 5
# Вывести цифры числа на каждой строчке.
number = 56229
while number>0:
    print(number%10)
    number = number//10
'''


'''
# Задача 6
# Найти сумму цифр числа.

sum = 0
number = 56987
while number>0:
    sum += number % 10
    number = number//10
print(sum)
'''


'''
# Задача 7
# Найти произведение цифр числа.

multiplication = 1
number = 56743
while number>0:
    multiplication *= number % 10
    number = number//10
print(multiplication)
'''


'''
# Задача 8
# Дать ответ на вопрос: есть ли среди цифр числа 5?

number = input('Введите число: ')
number = int(number)
while number>0:
    if number%10 == 5:
        print('5 есть в составе числа')
        break
    number = number//10
else: print('5 нет в составе числа')
'''


'''
# Задача 9
# Найти максимальную цифру в числе

number = input('Введите число: ')
number = int(number)
max_num = number%10
number = number//10
while number > 0:
    if number%10 > max_num:
        max_num = number%10
    number = number//10
print(max_num)
'''


'''
# Задача 10
# Найти количество цифр 5 в числе

count = 0
number = input('Введите число: ')
number = int(number)
while number>0:
    if number%10 == 5:
        count = count + 1

    number = number//10
print('Количество повторов числа 5: ', count)
'''