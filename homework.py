#1
out_f = open("my_file_0001.txt", "w")
inp = input("Введите новую строку. Для окончания введите пустую строку.")
while inp != "":
    out_f.write(f"{inp}\n")
    inp = input("Введите новую строку. Для окончания введите пустую строку.")

out_f.close()


#2
word = 0
words = []
for line in open("text_6.txt"):
    pos = 'out'
    for letter in line:
        if letter != ' ' and pos == 'out':
            word += 1
            pos = 'in'
        elif letter == ' ':
            pos = 'out'
    words.append(word)
    word = 0
print("Строк в указанном файле:", len(words))
for i in range(len(words)):
    print(f"В строке {i+1} - слов: {words[i]}")


#3
file = open("text_3.txt", "r", encoding="utf-8")
users = {}
for line in file:
    line = line.replace("\n", "")
    line = line.split(" ")
    users[line[0]] = float(line[1])
file.close()

print("Зарплаты менее 20 тыс. получают:")
for fio, oklad in users.items():
    if oklad < 20000:
        print(fio)

print(f"Зарплатный фонд: {sum(users.values())}")
print(f"Средняя зарплата на сотрудника ({len(users)} человек): {sum(users.values())/len(users)}")


#4
from deep_translator import GoogleTranslator
file = open("text_4.txt", "r", encoding="utf-8")
my_list = ""
for line in file:
    line = line.replace('\n', '').split(" - ")
    my_list = my_list + GoogleTranslator(source='auto', target='ru').translate(line[0]) + "\n"
file.close()

out_f = open("out_file.txt", "w")
out_f.write(my_list)
out_f.close()


#5
with open('file_5.txt', 'w+', encoding="utf-8") as file_obj:
    line = input('Введите цифры через пробел \n')
    file_obj.writelines(line)
    num = line.split()
    print(sum(map(int, num)))


#6
subj = {}
with open('text_6.txt', 'r', encoding="utf-8") as file:
    for line in file:
        lecture_int = practice_int = lab_int = 0

        subject, lecture, practice, lab = line.split()

        lecture_list = [int(num) for num in filter(lambda num: num.isnumeric(), lecture)]
        practice_list = [int(num) for num in filter(lambda num: num.isnumeric(), practice)]
        lab_list = [int(num) for num in filter(lambda num: num.isnumeric(), lab)]

        if type(lecture_list) == list and lecture_list != []:
            lecture_int = ''.join(str(e) for e in lecture_list)
        else:
            lecture_int = 0
        if type(practice_list) == list and practice_list != []:
            practice_int = ''.join(str(e) for e in practice_list)
        else:
            practice_int = 0
        if type(lab_list) == list and lab_list != []:
            lab_int = ''.join(str(e) for e in lab_list)
        else:
            lab_int = 0

        print(f"Общее количество часов по {subject} {int(lecture_int) + int(practice_int) + int(lab_int)}")


#7
import json

profit = {}
pr = {}
prof = 0
prof_aver = 0
i = 0
with open('text_7.txt', 'r+', encoding="utf-8") as file:
    for line in file:
        f_n, name, earning, damage = line.split()
        profit[name] = int(earning) - int(damage)
        if profit.setdefault(name) >= 0:
            prof = prof + profit.setdefault(name)
        i += 1
        if i >= 0:
            prof_aver = prof / i
    else:
        pr_sr = ({'Средняя прибыль компаний': round(prof_aver)})
        profit.update(pr_sr)
    print(f'Прибыль всех компании: - {prof:.2f}')
    print(f'Средняя прибыль всех компаний: - {round(prof_aver):.2f}')
    print(f'Сводные результаты компаний: - {profit}')

with open('test_7.json', 'w+', encoding="utf-8") as write_js:
    json.dump(profit, write_js)
print(json.dumps(profit), ensure_ascii=False)