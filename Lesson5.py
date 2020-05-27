# Task1. Создать программно файл в текстовом формате, записать в него построчно данные,
# вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.

out_str = input('Введите данные через пробел, enter чтобы закончить:').split()
with open("out_file.txt", "w") as out_file:
    for el in out_str:
        out_file.write('%s\n' % el)

# Task2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

inp_list = ['Создать текстовый файл (не программно),\n',
            'сохранить в нем несколько строк,\n',
            'выполнить подсчет количества строк,\n',
            'количества слов в каждой строке.\n'
            ]
with open("Task2.txt", 'w+') as out_file:
    out_file.writelines(inp_list)

counter_lines = 0
count_lines = []
count_words = []
with open("Task2.txt", "r") as in_file:
    file_lines = in_file.readlines()
    for line in file_lines:
        counter_lines += 1
        count_lines.append(counter_lines)
    count_words = [len(line.split(' ')) for line in file_lines]

print(*('{} -- {}'.format(*item) for item in zip(count_lines, count_words)), sep='\n')

# Task3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их
# окладов. Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

inp_list = {'Иванов': '31500.5',
            'Смирнов': '9100.1',
            'Петров': '20300',
            'Федоров': '10800.5',
            'Борисов': '5000',
            'Андреев': '21300',
            'Владимиров': '45000.8',
            'Афанасьев': '7500',
            'Геннадьев': '19700.5',
            'Филиппов': '8500',
            'Филимонов': '10000'
            }
with open("Task3.txt", 'w+') as out_file:
    for name, salary in inp_list.items():
        out_file.write(name + "\t" + salary + "\n")

with open("Task3.txt", "r") as in_file:
    file_lines = in_file.read().splitlines()
    for line in file_lines:
        list_lines = [line.split("\t") for line in file_lines]
        try:
            list_salaries = [float(a[1]) for i, a in enumerate(list_lines)]
            list_people = [a[0] for i, a in enumerate(list_lines) if float(a[1]) < 20000]
            avg_salary = sum(list_salaries)/len(list_salaries)
        except ValueError:
            print("Не числовое значение з/п")

print("Средняя з/п: {:.2f}".format(avg_salary))
print("Сотрудники с з/п меньше 20 тыс.р.:", *('{}'.format(people) for people in list_people), sep='\n')


# Task4 Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно
# данные. При этом английские числительные должны заменяться на русские. Новый блок строк
# должен записываться в новый текстовый файл.

inp_list = {'One': '1',
            'Two': '2',
            'Three': '3',
            'Four': '4'
            }
with open("Task4.txt", 'w+') as out_file_0:
    for key, value in inp_list.items():
        out_file_0.write(key + " - " + value + "\n")

dict_trans = {'One': 'Один', 'Three': 'Три', 'Two': 'Два', 'Four': 'Четыре'}
rus_list = []
with open("Task4.txt", "r") as in_file:
    file_lines = in_file.read().splitlines()
    for line in file_lines:
        line_sep = line.split(" - ")
        if line_sep[0] in dict_trans:
            rus_key = dict_trans[line_sep[0]]
            rus_list.append(rus_key + " - " + line_sep[1] + "\n")

with open("Task4_RUS.txt", 'w+') as out_file_1:
    out_file_1.writelines(rus_list)


# Task5 Создать (программно) текстовый файл, записать в него программно набор чисел,
# разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить
# ее на экран.

while True:
    try:
        inp_str = input('Введите числа через пробел, enter чтобы закончить:').split()
        out_str = [float(i) for i in inp_str]
        break
    except ValueError:
        print("Введите числовые значения")
        continue

with open("Task5.txt", "w+") as out_file:
    out_file.write(' '.join(inp_str) + ' ')
print("Сумма чисел равна: {:.2f}".format(sum(out_str)))


# Task6 Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный
# предмет и наличие лекционных, практических и лабораторных занятий по этому предмету и их
# количество. Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по
# нему. Вывести словарь на экран.
# Примеры строк файла: Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
# Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

from functools import reduce

subject_list = []
school_dict = {}
with open("Task6.txt", "r") as in_file:
    file_lines = in_file.read().splitlines()
    for line in file_lines:
        line_sep = line.split(" ")
        hours_list = []
        for item in line_sep:
            nums_str = ''.join(filter(lambda i: i.isdigit(), item))
            subject = str(line_sep[0])[:-1]
            try:
                hours = float(nums_str)
                hours_list.append(hours)
                result = reduce(lambda a, b: a + b, hours_list)
                school_dict[subject] = result
            except ValueError:
                pass
    print(school_dict)


# Task7 Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая
# строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также
# среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а
# также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в
# словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{ "firm_1" : 5000 , "firm_2" : 3000 , "firm_3" : 1000 }, { "average_profit" : 2000 }]
# Подсказка: использовать менеджер контекста.

import json
profit = {}
avg_add = {}
i = 0
profit_p = 0
with open('Task7.txt', 'r') as file:
    for line in file:
        name, structure, turnover, expences = line.split()
        try:
            profit[name] = float(turnover) - float(expences)
            if profit.setdefault(name) >= 0:
                i += 1
                profit_p = profit_p + float(turnover) - float(expences)
                avg_profit = profit_p / i
                # print(avg_profit)
        except ValueError:
            print('Невозможно преобразовать в числовые значения')
    if i != 0:
        print(f'Средняя прибыль среди безубыточных - {avg_profit:.2f}')
    else:
        print('Все фирмы убыточны')
    avg_add = {'Средняя прибыль': round(avg_profit)}
    profit.update(avg_add)
    print(f'Список значений:{profit}')

with open('Task7.json', 'w+') as new_json:
    json.dump(profit, new_json)
    json_data = json.dumps(profit, ensure_ascii=False)
    print(json_data)
