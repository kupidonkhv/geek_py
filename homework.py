#1
class Matrix:
    def __init__(self, lists):
        self.lists = lists

    def __str__(self):
        for row in self.lists:
            for i in row:
                print(f"{i:4}", end="")
            print()
        return ''

    def __add__(self, other):
        if len(self.lists) == len(other.lists):
            what_is_the_matrix = []
            for i in range(len(self.lists)):
                if len(self.lists[i]) == len(other.lists[i]):
                    second_matrix = []
                    for a in range(len(other.lists[i])):
                        second_matrix.insert(a, self.lists[i][a] + other.lists[i][a])
                    what_is_the_matrix.insert(i, second_matrix)
                else:
                    print("Матрицы разного размера!")
                    return
            return Matrix(what_is_the_matrix) #Сложение более 2-х матриц. Сделал для себя, чтоб понять.
        else:
            print("Матрицы разного размера!")
            return


m_1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
m_2 = Matrix([[7, 6, 5], [4, 33, 12], [14, 11, -5]])
m_3 = Matrix([[7, 6, 5], [4, 33, 12], [14, 11, -5]])
print(type(m_1 + m_2))
print(m_1 + m_2)
print(m_1 + m_2 + m_3)


#1 - Вариант с numpy.. numpy КРУТ!!!
import numpy as np


class Matrix:
    def __init__(self, lists):
        self.lists = lists

    def __str__(self):
        for row in self.lists:
            for i in row:
                print(f"{i:4}", end="")
        return

    def __add__(self, other):
        try:
            return np.array(self.lists) + np.array(other.lists)
        except ValueError:
            return "Матрицы разного размера!"


m_1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
m_2 = Matrix([[7, 6, 5], [4, 33, 12], [14, 11, -5]])
print(m_1 + m_2)


#2
from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, param):
        self.param = param

    def __str__(self):
        return f"{self.param}"

    @property
    def t_summ(self):
        return f'Сумма затраченной ткани равна: {self.param / 6.5 + 0.5 + (2 * self.param + 0.3) / 100 :.2f}'


class Coat(Clothes):
    def count(self):
        return f"На пальто ушло ткани: {self.param / 6.5 + 0.5 :.2f}"


class Suit(Clothes):
    def count(self):
        return f"На костюм ушло ткани: {(2 * self.param + 0.3) / 100 :.2f}"


coat = Coat(22)
suit = Suit(22)
print(coat.count())
print(suit.count())
print(coat.t_summ)


#3
class Cell:
    def __init__(self, quantity):
        self.quantity = quantity

    def make_order(self, rows):
        result = ''
        for i in range(int(self.quantity // rows)):
            result += '@' * rows + '\n'
        result += '@' * (self.quantity % rows) + '\n'
        return result

    def __str__(self):
        return f'{self.quantity}'

    def __sub__(self, other):
        return Cell(self.quantity - other.quantity)

    def __truediv__(self, other):
        return Cell(self.quantity // other.quantity)

    def __mul__(self, other):
        return Cell(self.quantity * other.quantity)

    def __add__(self, other):
        return Cell(self.quantity + other.quantity)


cell = Cell(4)
cell_2 = Cell(30)
print(cell + cell_2)
print(cell - cell_2)
print(cell * cell_2)
print(cell / cell_2)

print(cell_2.make_order(9))
