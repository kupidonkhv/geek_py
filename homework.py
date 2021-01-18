#1
result_list = ['Lorem', 'Ipsum', '-', 'это', 'текст-рыба', 'часто', 'используемый', 'в', 'печати', 'и', 'вэб-дизайне', '11131251', 11]

for i in range(len(result_list)):
    print(type(result_list[i]))

#2
my_list = list(input("Введите число:"))
for i in range(len(my_list)):
    if i%2 == 0:
        tmp_var = my_list[i]
    else:
        my_list[i-1] = my_list[i]
        my_list[i] = tmp_var
print(my_list)

#3
month = 13
year = dict(mon_1=['Январь','зима'], mon_2=['Февраль','зима'], mon_3=['Март','весна'], mon_4=['Апрель','весна'],
            mon_5=['Май','весна'], mon_6=['Июнь','лето'], mon_7=['Июль','лето'], mon_8=['Август','лето'],
            mon_9=['Сентябрь','осень'], mon_10=['Октябрь','осень'], mon_11=['Ноябрь','осень'], mon_12=['Декабрь','зима'])
mon_list = ('mon_1','mon_2','mon_3','mon_4','mon_5','mon_6','mon_7','mon_8','mon_9','mon_10','mon_11','mon_12')
while month >= 12:
    month = int(input("Введите номер месяца (смею напомнить, что месяцев в году всего 12!)"))
print(f"Вы ввели {month} это {year[mon_list[month-1]][0]}, и он относится к веремени года \"{year[mon_list[month-1]][1]}\"")

#4
inp = input("Введите строку из нескольких слов, разделённых пробелами").split(" ")
for i in range(len(inp)):
    if(len(inp[i]) >= 10):
        print(inp[i][0:10])
    else:
        print(inp[i])

#5
rate = [7, 5, 3, 3, 2]
inp = int(input("Введите новый элемент рейтинга:"))
while inp != "!!!!":
    place = 0 if rate[0] < inp else len(rate)
    for i in range(len(rate)):
        if inp > rate[i] and place > 0:
            place = rate.index(rate[i])
    rate.insert(place, inp)
    inp = input(f"{rate}\nВведите новый элемент рейтинга (для выхода введите \"x\"):")
    if inp == "x":
        quit("EXIT!")
    else:
        inp = int(inp)

#6
inp = ""
result_list = []
result_list.append([(1,{"название": "компьютер", "цена": 20000, "количество": 5, "eд": "шт.",})])
result_list.append([(2,{"название": "принтер", "цена": 6000, "количество": 3, "eд": "шт.",})])
result_list.append([(3,{"название": "сканер", "цена": 2000, "количество": 7, "eд": "шт.",})])
while inp != "x":
    print("Меню:\n1. добавления товара\n2. аналитика\n3. выход")
    inp = int(input("Выберите пункт меню:"))
    if inp == 1:
        c_name = input("название")
        c_price = int(input("цена"))
        c_quantity = int(input("количество"))
        с_unit_of_measure = input("единица измерения")
        result_list.append([(len(result_list)+1, {"название": str(c_name), "цена": c_price, "количество": c_quantity, "eд": str(с_unit_of_measure)})])
        print(result_list)
    elif inp == 2:
        d = {'название': [], 'цена': [], 'количество': [], 'ед': [], }
        for i in range(len(result_list)):
            d['название'].append(result_list[i][0][1]['название'])
            d['цена'].append(result_list[i][0][1]['цена'])
            d['количество'].append(result_list[i][0][1]['количество'])
            d['ед'].append(result_list[i][0][1]['eд'])
        print(d)
    elif inp == 3:
        quit("EXIT!")
    else: print("Нет такого пункта! Повторите ввод!")









