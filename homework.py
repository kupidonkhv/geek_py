#1
class DataForrmatterrr:
    def __init__(self, inp_date):
        self.inp_date = inp_date.split('-')

    @classmethod
    def format_date(cls, inp_date):
        try:
            day, month, year = [int(el) for el in inp_date.split('.')]
            format_date_type = '{0}\n{1}\n{2}'.format((type(day), day), (type(month), month), (type(year), year))
            return format_date_type
        except ValueError:
            return 'Некорректный формат даты.'

    @staticmethod
    def validate(inp_date):
        try:
            day, month, year = inp_date.split('.')
            datetime.date(int(year), int(month), int(day))
            return 'Корректный формат даты.'
        except ValueError:
            return 'Некорректный формат даты.'


print('Вы записали: {0}'.format('05-03-2020'))
print(DataForrmatterrr.validate('05-03-2020'))
print('Вы записали: {0}'.format('02-02'))
print(DataForrmatterrr.format_date('02-02'))
print('Вы записали: {0}'.format('4445465474'))
print(DataForrmatterrr.format_date('5454354354684313857'))
print('Вы записали: {0}'.format('1-45-51'))
print(DataForrmatterrr.validate('1-45-51'))


#2
class DivZero(Exception):
    def __init__(self, pos_arg):
        self.pos_arg = pos_arg


def division(param_1, param_2):
    if param_2 == 0:
        raise DivZero('Невозможно деление на ноль')
    else:
        param_res = param_1 / param_2
        print('При делении {0} на {1} получилось {2}'.format(param_1, param_2, param_res))
    return param_1 / param_2


try:
    division(int(input('Делимое\n')), int(input('Делитель\n')))
except DivZero as pos_arg:
    print('{0}'.format(pos_arg))


#3
class ExceptionType(Exception):
    def __init__(self, param):
        self.text = param


list_num = []


def num_check(el):
    if el.isdigit():
        list_num.append(el)
    else:
        raise ExceptionType('Необходимо ввести только число')


while True:
    el = input('Введите число (для выхода введите stop)\n')
    try:
        if el == 'stop':
            print(list_num)
            break
        else:
            num_check(el)
    except ExceptionType:
        print('Необходимо ввести только число')


#4, 5, 6
class Sklad:

    def __init__(self, name, price, quantity, number_of_lists, *args):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.numb = number_of_lists
        self.my_store_full = []
        self.my_store = []
        self.my_unit = {'Модель устройства': self.name, 'Цена за ед': self.price, 'Количество': self.quantity}

    def __str__(self):
        return f'{self.name} цена {self.price} количество {self.quantity}'

    def reception(self):
        try:
            unit = input(f'Введите наименование ')
            unit_p = int(input(f'Введите цену за ед '))
            unit_q = int(input(f'Введите количество '))
            unique = {'Модель устройства': unit, 'Цена за ед': unit_p, 'Количество': unit_q}
            self.my_unit.update(unique)
            self.my_store.append(self.my_unit)
            print(f'Текущий список -\n {self.my_store}')
        except:
            return f'Ошибка ввода данных'

        print(f'Для выхода - Q, продолжение - Enter')
        q = input(f'---> ')
        if q == 'Q' or q == 'q':
            self.my_store_full.append(self.my_store)
            print(f'Весь склад -\n {self.my_store_full}')
            return f'Выход'
        else:
            return Sklad.reception(self)


class Printer(Sklad):
    def to_print(self):
        return f'to print smth {self.numb} times'


class Scanner(Sklad):
    def to_scan(self):
        return f'to scan smth {self.numb} times'


class Copier(Sklad):
    def to_copier(self):
        return f'to copier smth  {self.numb} times'


unit_1 = Printer('hp', 2000, 5, 10)
unit_2 = Scanner('Canon', 1200, 5, 10)
unit_3 = Copier('Xerox', 1500, 1, 15)
print(unit_1.reception())
print(unit_2.reception())
print(unit_3.reception())
print(unit_1.to_print())
print(unit_3.to_copier())


#7
class ComplexNumber:
    def __init__(self, a, b, *args):
        self.a = a
        self.b = b
        self.z = 'a + b * i'

    def __add__(self, other):
        print(f'Сумма z1 и z2 равна')
        return f'z = {self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        print(f'Произведение z1 и z2 равно')
        return f'z = {self.a * other.a - (self.b * other.b)} + {self.b * other.a} * i'

    def __str__(self):
        return f'z = {self.a} + {self.b} * i'


z_1 = ComplexNumber(1, -2)
z_2 = ComplexNumber(3, 4)
print(z_1)
print(z_1 + z_2)
print(z_1 * z_2)
