from sys import argv
from functools import reduce
from itertools import cycle
import math

#1
script_name, hours, price, premia = argv
print(f"Зарплата сотрудника: {(int(hours)*int(price))}; Премия: {premia}; Итого: {(int(hours)*int(price))+int(premia)}")


#2
x = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
y = [i for n,i in enumerate (x) if x[n]> x[n-1]]
print(f'Result: {y}')


#3
print(f'Result: {[i for n,i in enumerate (range (20,241)) if i % 20 ==0 or i % 21 ==0]}')


#4
x = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print(f'Result: {[i for n,i in enumerate (x) if x.count(i)==1]}')


#5
print(reduce(lambda x, y: x + y, list(range(100, 1001, 2))))


#6 а)
script_name, start, end = argv
my_list = list(range(int(start), int(end)+1))
for i, x in enumerate(my_list):
    print(x)


#6 б)  выводит в строку
script_name, text, count = argv
my_list = list("ABC" * int(5))
print(''.join(my_list))


#6 б) - ещё вариант (выводит построчно):
script_name, text, count = argv
с = int(1)
for el in cycle([text]):
    if с >= int(count):
        break
    print(el)
    с += 1

#7
script_name, num = argv


def fact():
    for i in range(1, int(num)):
        yield math.factorial(i)


for i in fact():
    print(f"Объект: {fact()}; Факториал: {i}")