# задание 1
inp_name = input('Ваше имя?\n')

while True:
    inp_age = input('Ваш возраст?\n')
    if inp_age.isdigit():
        inp_age = int(inp_age)
        break
    else:
        print('Неверный возраст', inp_name, '=))\nПопробуйте еще раз')
var_str = 'Добрый день, {}, Вам {}'.format(inp_name, inp_age)
print(var_str)

list_quar = ['да', 'Да', 'нет', 'Нет', 'ага', 'Ага', 'yes', 'Yes', 'no', 'No']
list_quar_yes = ['да', 'Да', 'ага', 'Ага', 'yes', 'Yes']
list_quar_no = ['нет', 'Нет', 'no', 'No']
while True:
    inp_quar = input('Вы на карантине?Да/Нет\n')
    if inp_quar in list_quar:
        if inp_quar in list_quar_yes:
            print(inp_name, ', даже если Вы на карантине, все будет хорошо=)')
        else:
            print(inp_name, ', Вам повезло, Вы не на карантине!')
        break
    else:
        print('Введите да или нет,', inp_name, '=))')
print('Едем дальше')

# задание 2

while True:
     inp_sec = input('Пожалуйста, введите время в секундах\n')
     if inp_sec.isdigit():
         inp_sec = int(inp_sec)
         seconds = inp_sec % (24 * 3600)
         hours = seconds // 3600
         seconds %= 3600
         minutes = seconds // 60
         seconds %= 60
         # print('{:>02}:{:>02}:{:>02}'.format(hours, minutes, seconds))
         # print('{:02d}:{:>02d}:{:>02d}'.format(hours, minutes, seconds))
         print('%02d:%02d:%02d' % (hours, minutes, seconds))
         break
     else:
         print('Подумайте еще,', inp_name)
print('Такой получился формат')

# задание 3

while True:
    inp_n = input('Введите любое число n\n')
    if inp_n.isdigit():
        inp_n1 = int(inp_n)
        inp_n2 = inp_n1*10 + inp_n1
        inp_n3 = inp_n1 * 100 + inp_n2
        inp_sum = inp_n1 + inp_n2 + inp_n3
        print(inp_sum)
        break
    else:
        print('Попробуйте еще раз, только теперь число')
print('Это сумма n + nn + nnn')

# задание 4

while True:
    inp_num = input('Введите целое положительное число\n')
    if inp_num.isdigit():
        num = int(inp_num)
        list_num = [int(x) for x in str(num)]
        print(str(list_num), ' - это сами числа')
        print(max(list_num), ' - это самое больше число из них')
        break
    else:
        print('Попробуйте еще раз, только теперь целое положительное')
print('Получилось так')

# задание 5

while True:
    rev = input('Введите показатель выручки\n')
    exp = input('Введите показатель расходов\n')
    if rev.isdigit() and exp.isdigit():
        profit = int(rev)-int(exp)
        if profit >= 0:
            profitab = profit / int(rev)
            print('Фирма работает с прибылью: {} \nРентабельность:{:.1%}'.format(profit, profitab))
            while True:
                fte = input('Введите численность сотрудников\n')
                if fte.isdigit():
                    profit_per_fte = profit / int(fte)
                    # print('Прибыль в расчете на одного сотрудника: {:.1f}'.format(profit_per_fte))
                    break
                else:
                    print('Число сотрудников должно быть числом')
                    continue
            print('Фирма работает с прибылью: {} \nРентабельность:{:.1%}\nПрибыль на сотрудника:{:.1f}'.format(profit, profitab, profit_per_fte))
        else:
            print('Фирма работает с убытком:', profit)
        break
    else:
        print('Введите числовые показатели')
print('Это расчет прибыли')


# задание 6

while True:
    km_start = input('Сколько км в первый день?\n')
    km_fin = input('Сколько км всего нужно пробежать?\n')
    if km_start.isdigit() and km_fin.isdigit():
        km_start = int(km_start)
        km_fin = int(km_fin)
        if km_start > km_fin:
            print('Общее число км должно быть больше')
            continue
        else:
            count = 1
            while km_fin > km_start:
                km_start = km_start * 1.1
                count += 1
                # print(km_start, count)
        break
    else:
        print('Введите чиcла')
print('Вы достигнете результата на день', count)
