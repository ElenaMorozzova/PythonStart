# Task1 Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv
print('Расчет заработной платы. Вы ввели через пробел 3 значения - ')
_, hours, sal_per_hours, bonus = argv
print("Отработанные часы:", str(argv[1]))
print("З/п в час:", str(argv[2]))
print("Доп. бонус:", str(argv[3]))
for arg in argv:
    try:
        salary = float(hours) * float(sal_per_hours) + float(bonus)
        break
    except ValueError as e:
        print("Введите числовые аргументы")
        continue

print(f' Заработная плата итого равна: {salary}')

