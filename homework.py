#1
def func_1(var_1, var_2):
    try:
        print(var_1 / var_2)
    except ZeroDivisionError:
        print("division by zero")


var_1 = int(input("Введите число 1"))
var_2 = int(input("Введите число 2"))
func_1(var_1, var_2)


#2
var = ['имя', 'фамилия', 'год рождения', 'город проживания', 'email', 'телефон']
dict = {}
for i in range(len(var)):
    dict[var[i]] = input(f"Введите {var[i]}")


def user_info(**dict):
    print('; '.join('{}-{}'.format(key, value) for key, value in dict.items()))


user_info(**dict)


#3
def my_func(arg_1, arg_2, arg_3):
    list = []
    list.append(arg_1)
    list.append(arg_2)
    list.append(arg_3)
    list.remove(min(list))
    print(sum(list))


my_func(1, 2, 5)


#4
def my_func(x, y):
    ret = 0
    for i in range(abs(y)):
        ret += x
    return 1/ret


print(my_func(2, -2))


#5
def my_func(data):
    global summ
    summ = summ+sum(list(map(int, data.split())))
    print(summ)


data = 1
summ = 0
while data:
    data = input("Введите строку чисел, разделенных пробелом (для выхода введите \"x\"):")
    if "x" in data:
        my_func(data.replace("x", ''))
        quit()
    else:
        my_func(data)


#6
def int_func(word):
    word = list(word)
    word[0] = word[0].upper()
    return "".join(word)


def test_ord(test_):
    test_ = list(lorem)
    for i in range(len(test_)):
        if ord(test_[i]) not in range(97, 123) and ord(test_[i]) != 32 and test_[i] not in ['!', '&', '?', '.', ',', '-', '$']:
            print(f"Некорректный символ \"{test_[i]}\"")
            return 0


lorem = input("Введите произвольное количество слов из латинских букв в нижнем регистре")
if test_ord(lorem) == 0:
    print("Ошибка! Введён некорректный символ!")
else:
    lorem = lorem.split(" ")
    for i in range(len(lorem)):
        lorem[i] = int_func(lorem[i])
    lorem = " ".join(lorem)

    print(lorem)