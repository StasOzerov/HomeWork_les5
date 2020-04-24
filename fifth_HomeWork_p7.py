
# 7 p -------------------------------------------------

'''
Создать (не программно) текстовый файл,
в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.

Необходимо построчно прочитать файл, вычислить прибыль каждой компании,
а также среднюю прибыль. Если фирма получила убытки,
в расчет средней прибыли ее не включать.

Далее реализовать список.
Он должен содержать словарь с фирмами и их прибылями,
а также словарь со средней прибылью. Если фирма получила убытки,
также добавить ее в словарь (со значением убытков). Пример списка:
[{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].

Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
'''

import json

dict_firms = {}
all_profit = i = k = 0

try:
    with open('ДЗ 7 пункт.txt', 'r') as f_rd:
        for line in f_rd:
            i += 1
            my_li = line.split()
            try:
                if len(my_li) == 4:
                    my_li[2] = int(my_li[2])
                    my_li[3] = int(my_li[3])
                    profit = my_li[2] - my_li[3]
                    if profit > 0:
                        all_profit += profit
                        k += 1
                    dict_tmp = {my_li[0]: profit}
                    dict_firms.update(dict_tmp)
                else:
                    print(f'В строке {i} количество позиций не равно 4-м')
            except ValueError:
                print(f'Некорректные данные по выручке/издержке! (строка {i})')
except IOError:
    print('Ошибка ввода-вывода')

complex_list = [dict_firms, {'Средняя прибыль': int(all_profit / k)}]
print(complex_list)

with open("ДЗ 7 пункт перезаписанный.json", "w", encoding='UTF-8') as f_wr:
    json.dump(complex_list, f_wr, ensure_ascii=False)
