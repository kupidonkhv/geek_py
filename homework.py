#1
from time import sleep


class SvetoFor:
    __text = ['Красный', 'Желтый', 'Зеленый']
    __color = ['\033[31m {}', '\033[33m {}', '\033[32m {}']

    def runn(self):
        i = 0
        while i != 3:
            print(SvetoFor.__color[i].format(SvetoFor.__text[i]))
            if i == 0:
                sleep(7)
            elif i == 1:
                sleep(2)
            elif i == 2:
                sleep(5)
            i += 1


while True:
    t = SvetoFor()
    t.runn()


#2
class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width
        self.weight = 25
        self.height = 5

    def asphalt_mass(self):
        asphalt_mass = self._length * self._width * self.weight * self.height / 1000
        print(f'масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см: {round(asphalt_mass)}')


r = Road(5000, 20)
r.asphalt_mass()


#3
class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": int(wage), "bonus": int(bonus)}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]


p = Position('Сергей', 'Алексейцев', 'Кодер', '100000', '100000')
print(p.get_full_name(), p.get_total_income())


#4
class Car:

    def __init__(self, name, speed, color, is_police=False):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

    def go(self):
        return f'Машина {self.name} поехала.'

    def stop(self):
        return f'\n{self.name} остановилась.'

    def turn(self, direction):
        return f'\nМашина {self.name} повернула {direction}'

    def show_speed(self):
        return f'\nСкорость машины: {self.speed}'


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'\nПревышении скорости {self.speed}!'


class SportCar(Car):
    def show_speed(self):
        if self.speed > 300:
            return f'\nПревышении скорости {self.speed}!'


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'\nПревышении скорости: {self.speed}'


class PoliceCar(Car):
    def turn_on_flashing_light(self):
        return f'\nИииииууу Иииииууу Иииииууу Иииииууу!'

    def piu_piu(self):
        return f'\nСтреляем по преследуему!'


town = TownCar('Audi TT', 70, 'blue', False)
print(town.go(), town.show_speed(), town.turn('направо'), town.turn('направо'), town.stop())

sport = SportCar('Lamborghini Diablo', 170, 'синяя', False)
print(sport.go(), sport.show_speed(), sport.turn('налево'), sport.stop())

work = WorkCar('МАЗ', 30, 'красная', False)
print(work.go(), work.show_speed(), work.turn('направо'), work.stop())

police = PoliceCar('Бэтмобиль', 100, 'жёлтая', True)
print(police.go(), police.turn_on_flashing_light(), police.show_speed(), police.turn('полицейский разворот'), police.go(), police.turn('направо'), police.piu_piu(), police.stop())


#5
class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f'Запуск отрисовки'


class Pen(Stationery):
    def draw(self):
        return f'Запуск отрисовки {self.title}'


class Pencil(Stationery):
    def draw(self):
        return f'Запуск отрисовки {self.title}'


class Handle(Stationery):
    def draw(self):
        return f'Запуск отрисовки {self.title}'


pen = Pen('ручкой')
print(pen.draw())
pencil = Pencil('карандашем')
print(pencil.draw())
handle = Handle('маркером')
print(handle.draw())