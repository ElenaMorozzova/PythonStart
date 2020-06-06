# Task1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде
# строки формата «день-месяц-год». В рамках класса реализовать два метода. Первый, с
# декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к
# типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
# месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на
# реальных данных.


class MyData:
    def __init__(self, str_date):
        self.str_date = str_date

    @classmethod
    def data_to_num(cls, str_date):
        day, month, year = map(int, str_date.split('-'))
        print(f'Это числовые значения даты: {day}, {month}, {year}')

    @staticmethod
    def is_valid(str_date):
        day, month, year = map(int, str_date.split('-'))
        if day <= 31 and month <= 12 and year <= 2050:
            print('Дата допустимая')
        else:
            print('Дата не прошла проверку')


MyData.data_to_num('01-01-2020')
MyData.is_valid('45-01-2020')

# Task2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля в
# качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с
# ошибкой.


class DelError(Exception):
    def __init__(self, *args):
        self.args = args
        pass


try:
    num_1 = input('Введите числитель:\n')
    num_2 = input('Введите знаменатель:\n')
    if float(num_2) == 0:
        raise DelError('Делить на ноль нельзя')
except ValueError:
    print('Введите числовые значения')
except DelError as err:
    print(err)
else:
    print(f'Результат деления равен: {float(num_1) / float(num_2)}')

# Task3.Создайте собственный класс-исключение, который должен проверять содержимое списка на
# наличие только чисел. Проверить работу исключения на реальном примере. Необходимо
# запрашивать у пользователя данные и заполнять список только числами. Класс-исключение
# должен контролировать типы данных элементов списка.
# Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока
# пользователь сам не остановит работу скрипта, введя, например, команду “stop”. При этом
# скрипт завершается, сформированный список с числами выводится на экран.
# Подсказка: для данного задания примем, что пользователь может вводить только числа и
# строки. При вводе пользователем очередного элемента необходимо реализовать проверку
# типа элемента и вносить его в список, только если введено число.
# Класс-исключение должен не позволить пользователю ввести текст (не число) и отобразить
# соответствующее сообщение. При этом работа скрипта не должна завершаться


class InputError(Exception):
    def __init__(self, *args):
        self.args = args

    def __str__(self):
        return f'Вы ввели не числовое значение, оно не будет добавлено в список'
        pass


q_list = ['q', 'Q', 'stop', 'STOP']
float_list =[]
ex = False
while not ex:
    nums = input('Введите числа через Enter, чтобы выйти нажмите q или stop:\n').split('\n')
    for i in range(len(nums)):
        if str(nums[i]) in q_list:
            ex = True
            print(float_list)
            break
        else:
            try:
                float_num = [float(itm) for itm in nums]
                float_list.extend(float_num)
            except ValueError as err:
                print(InputError())
                pass

# Task4-6 Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А
# также класс «Оргтехника», который будет базовым для классов-наследников. Эти классы —
# конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определить
# параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
# уникальные для каждого типа оргтехники.

# Разработать методы, отвечающие за приём
# оргтехники на склад и передачу в определенное подразделение компании. Для хранения
# данных о наименовании и количестве единиц оргтехники, а также других данных, можно
# использовать любую подходящую структуру, например словарь.

# Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на
# склад, нельзя использовать строковый тип данных.

from abc import ABC, abstractmethod


class Warehouse(ABC):
    @abstractmethod
    def __str__(self):
        pass


class OfficeEquip(Warehouse):
    def __init__(self, name, model, quantity, sell_price, cost_price, to_shop=None):
        self.name = name
        self.to_shop = to_shop
        self._params = {"Model": model, "Quantity": quantity,
                        "Sell_price": sell_price, "Cost_price": cost_price
                        }

    def __str__(self):
        return f'{self.name} {self._params.get("Model")} \t ' \
               f'Цена: {self._params.get("Sell_price")} ' \
               f'Количество: {self._params.get("Quantity")}'

    @property
    def q_valid(self):
        quantity = self._params.get("Quantity")
        model = self._params.get("Model")
        name = self.name
        try:
            if int(quantity) > 0:
                return f'Допустимое количество товара {name} {model}'
            else:
                return f'Количество товара {name} {model} недопустимое'
        except ValueError:
            return f'Введите числовое значение количества товара {name} {model}'

    def move(self, to_shop):
        return f'Данный товар должен быть направлен со склада в подразделение {to_shop}'


class Printer(OfficeEquip):
    def __init__(self, *args):
        super().__init__(*args)

    def wh_place(self):
        return f'Данный товар хранится на складе в секции А'


class Scanner(OfficeEquip):
    def __init__(self, *args):
        super().__init__(*args)

    def wh_place(self):
        return f'Данный товар хранится на складе в секции В'


class Xerox(OfficeEquip):
    def __init__(self, *args):
        super().__init__(*args)

    def wh_place(self):
        return f'Данный товар находится в секции С'


eq_1 = OfficeEquip('Принтер', 'XP 4500', -7, 1500, 1000)
eq_2 = Scanner('Сканер', 'Canon 870', 3, 1500, 1000)
eq_3 = Printer('Принтер', 'XP 4500', -7, 1500, 1000)
eq_4 = Xerox('Ксерокс', 'Canon 870', 3, 1500, 1000)
print(eq_1)
print(eq_2)
print(eq_2.wh_place())
print(eq_3)
print(eq_4)
print(eq_1.q_valid)
print(eq_2.q_valid)
print(eq_3.q_valid)
print(eq_4.q_valid)
print(eq_2.move('Е1'))

# Task7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное
# число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив
# сложение и умножение созданных экземпляров. Проверьте корректность полученного
# результата.


class ComplexNumber:
    def __init__(self, a, b, *args):
        self.a = a
        self.b = b

    def __str__(self):
        try:
            a = int(self.a)
            b = int(self.b)
            if b < 0:
                return f'{a} - {-b}*i'
            else:
                return f'{a} + {b}*i'
        except ValueError:
            return f'Введите числовые значения'

    def __add__(self, other):
        b1 = self.b + other.b
        print(f'Сумма z1 и z2:')
        if b1 < 0:
            return f'{self.a + other.a} - {abs(self.b + other.b)} * i'
        else:
            return f'{self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        a1 = self.a * other.a - self.b * other.b
        b1 = self.a * other.b + self.b * other.a
        print(f'Умножение z1 и z2:')
        if b1 < 0:
            return f'{a1} - {abs(b1)} * i'
        else:
            return f'{a1} + {b1} * i'


z_1 = ComplexNumber(2, -4)
z_2 = ComplexNumber(1, 3)
print(f'Комплексное число 1: {z_1}\nКомплексное число 2: {z_2}')
print(z_1 + z_2)
print(z_1 * z_2)
