# Задание 1. Реализовать функцию, принимающую два числа (позиционные аргументы)
# и выполняющую их деление. Числа запрашивать у пользователя, предусмотреть обработку
# деления на ноль.
from numpy.core.defchararray import capitalize


def div_calc():
    while True:
        try:
            a = float(input("Укажите число 1:"))
            b = float(input("Укажите число 2:"))
            result = a / b
            return result
            break
        except ZeroDivisionError:
            print("Делить на ноль нельзя, но пусть будет ноль")
            result = 0
            return result
            break
        except ValueError as error:
            print("Введите числовые аргументы")
            continue


result = div_calc()
print(result)

# Задание 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.


def user_profile():
    name = capitalize(input("Укажите имя:"))
    sname = capitalize(input("Укажите фамилию:"))
    city = capitalize(input("Укажите город проживания:"))
    while True:
        byear = input("Укажите год рождения:")
        if byear.isdigit() and 1900 <= int(byear) <= 2020:
            byear = int(byear)
            break
        else:
            print('Введите корректный год рождения')
            continue
    while True:
        email = input("Укажите email:")
        if "@" in email and len(email) > 5:
            email = email.lower()
            break
        else:
            print('Введите корректный email')
            continue
    while True:
        phone = input("Укажите телефон после (+7):")
        if phone.isdigit() and len(phone) == 10:
            phone = int(phone)
            break
        else:
            print('Введите корректный телефон (10 цифр)')
            continue
    return name, sname, city, byear, email, phone


name_v, sname_v, city_v, byear_v, email_v, phone_v = user_profile()
print('Вас зовут - ', name_v, sname_v, ',', byear_v, 'года рождения, место проживания - ', city_v, '. Ваш email:', email_v, '. Ваш тел.:', phone_v)

# 3. Реализовать функцию my_func(),
# которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.


def my_func():
    while True:
        try:
            a = int(input("Укажите число 1:"))
            b = int(input("Укажите число 2:"))
            c = int(input("Укажите число 3:"))
            min_val = min(a, b, c)
            if a == min_val:
                result = a + b
            elif b == min_val:
                result = a + c
            else:
                result = b + c
            return result
            break
        except ValueError as error:
            print("Введите числовые аргументы")
            continue


result = my_func()
print(result)


# 4. Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y.
# Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами.
# Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.

# Первый вариант
# функция на проверку целого числа

def is_integer(n):
    try:
        float(n)
    except ValueError:
        return False
    else:
        return float(n).is_integer()

def my_pov():
        while True:
            x = input("Укажите действительное положительное число x:")
            if float(x) > 0:
                x = float(x)
                break
            else:
                print('Введите действительное положительное число')
                continue
        while True:
            y = input("Укажите целое отрицательное число y:")
            if is_integer(y) and float(y) < 0:
                y = float(y)
                break
            else:
                print('Введите целое отрицательное число')
                continue
        res = x ** y
        return x, y, res


x_val, y_val, res_val = my_pov()
print('{:.1f} в степени {:.1f} будет:{:.8f}'.format(x_val, y_val, res_val))

# Второй вариант
def is_integer(n):
    try:
        float(n)
    except ValueError:
        return False
    else:
        return float(n).is_integer()


def my_pov():
    while True:
        x = input("Укажите действительное положительное число x:")
        if float(x) > 0:
            x = float(x)
            break
        else:
            print('Введите действительное положительное число')
            continue
    while True:
        y = input("Укажите целое отрицательное число y:")
        if is_integer(y) and float(y) < 0:
            y = float(y)
            break
        else:
            print('Введите целое отрицательное число')
            continue
    d = 1 / abs(x)
    i = 1
    while i < abs(y):
        d = 1 / -x * d
        # print(d)
        i += 1

    res = d
    return x, y, res


x_val, y_val, res_val = my_pov()
print('{:.1f} в степени {:.1f} будет:{:.8f}'.format(x_val, y_val, res_val))


# Задание 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел,
# разделенных пробелом и снова нажать Enter. Сумма вновь введенных чисел будет добавляться к уже
# подсчитанной сумме. Но если вместо числа вводится специальный символ, выполнение программы
# завершается. Если специальный символ введен после нескольких чисел, то вначале нужно добавить
# сумму этих чисел к полученной ранее сумме и после этого завершить программу.

def sum_list():
    q_list = ['q', 'Q', 'й', 'Й']
    sum_res: int = 0
    ex = False
    while not ex:
        num = input('Введите числа через пробел, чтобы выйти нажмите q:\n').split()
        res = 0
        try:
            for i in range(len(num)):
                if str(num[i]) in q_list:
                    ex = True
                    break
                else:
                    res = res + float(num[i])
        except ValueError as error:
            print("Введите числовые аргументы")
            continue
        sum_res = sum_res + res
        print(f'Сумма чисел: {sum_res}')
    print(f'Итоговая сумма: {sum_res}')


sum_list()


# Задание 6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и
# возвращающую его же, но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
# В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре.
# Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
# Необходимо использовать написанную ранее функцию int_func().
# def int_func():
#     res = capitalize(input("введите слово:\n"))
#     return res

def int_func(w):
    first_letter_s = w[0]
    first_letter_b = chr(ord(first_letter_s) - ord('z') + ord('Z'))
    return first_letter_b + w[1:]


print('Введите предложение:\n')
res = []
for w in map(str, input().split()):
    res.append(int_func(w))
print(' '.join(res))








