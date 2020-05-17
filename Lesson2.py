# Задание 1

var_list = [4, 0.5, 'hello', True, None, [1, 2, 3]]
for a in var_list:
    print(type(a))

# Задание 2

var_list1 = [4, 0.5, 'hello', True, None, [1, 2, 3]]
if len(var_list1) % 2 == 0:
    i = 0
    while i < len(var_list1):
        odd = var_list1[i]
        var_list1[i] = var_list1[i+1]
        var_list1[i+1] = odd
        i += 2
else:
    i = 0
    while i < len(var_list1) - 1:
        odd= var_list1[i]
        var_list1[i] = var_list1[i + 1]
        var_list1[i + 1] = odd
        i += 2
print(var_list1)


# Задание 3
var_calendar_list = [(1, "Зима"), (2, "Зима"), (3, "Весна"), (4, "Весна"), (5, "Весна"), (6, "Лето"),
                      (7, "Лето"), (8, "Лето"), (9, "Осень"), (10, "Осень"), (11, "Осень"), (12, "Зима")]
while True:
    month = input('Введите номер месяца\n')
    if month.isdigit():
        month = int(month)
        for a, b in var_calendar_list:
            if month == a:
                print('Время года -', b)
        break
    else:
        print('Номер месяца должен быть целым числом')
print('Сработало')

dict(var_calendar_list)
var_calendar_dict = {1: 'Зима', 2: 'Зима', 3: 'Весна', 4: 'Весна', 5: 'Весна', 6: 'Лето',
                      7: 'Лето', 8: 'Лето', 9: 'Осень', 10: 'Осень', 11: 'Осень', 12: 'Зима'}
while True:
    month = input('Введите номер месяца\n')
    if month.isdigit():
        month = int(month)
        for key, value in var_calendar_dict.items():
            if month == key:
                print('Время года -', value)
        break
    else:
        print('Номер месяца должен быть целым числом')
print('Сработало')


# Задание 4

var_str_list = list(input('Введите строку из нескольких слов\n').split(' '))
for index, a in enumerate(var_str_list):
    print('Номер строки: {} {:.10}'.format(index+1, a))

# Задание 5
rating_list = [7, 5, 3, 3, 2]
while True:
    new_item = input('Введите новый элемент списка\n')
    if new_item.isdigit():
        new_item = int(new_item)
        var_count = rating_list.count(new_item)
        for i, a in enumerate(rating_list):
            if var_count > 0:
                i = rating_list.index(new_item)
                rating_list.insert(i + var_count, new_item)
                break
                # print(i, a)
            else:
                if new_item > a:
                    # print(i, a)
                    n1 = rating_list.index(a)
                    # print(n1)
                    rating_list.insert(n1, new_item)
                    break
                elif new_item < a and new_item < rating_list[len(rating_list) - 1]:
                    rating_list.append(new_item)
        break
    else:
        print('Новый элемент списка должен быть целым числом')
print(rating_list)


# Задание 6

goods = int(input("Сколько товаров хотите записать:\n"))
goods_dict = []
goods_list = []
goods_matrix = {}
n = 1
while n <= goods:
    goods_dict = dict({'название': input("Название товара:\n"), 'цена': input("Цена товара:\n"),
                    'количество': input("Кол-во товара:\n"), 'eд': input("Ед. измерения:\n")})
    goods_list.append((n, goods_dict))
    n += 1
    goods_matrix = dict({'название': goods_dict.get('название'), 'цена': goods_dict.get('цена'),
    'количество': goods_dict.get('количество'), 'ед': goods_dict.get('eд')})
print('Лист товаров:', goods_list)
print('Характеристики товаров не получились:', goods_matrix)