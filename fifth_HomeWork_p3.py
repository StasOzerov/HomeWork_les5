
# 3 p -------------------------------------------------

'''
Создать текстовый файл (не программно),
построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
'''

import sys

li = []
sum_salary = i = k = 0
f = open('ДЗ 3 пункт.txt', 'r')
try:
    for line in f:
        k += 1
        li = line.split()
        if len(li) != 2:
            print('Ошибка в', k, 'строке файла!')
            sys.exit()
        tmp_dict = {li[0]:li[1]}
        for key in tmp_dict:
            try:
                if int(tmp_dict[key]) >= 0:
                    sum_salary += int(tmp_dict[key])
                    i += 1
                    if int(tmp_dict[key]) < 20000:
                        print(key, '- ЗП меньше 20000')
                else:
                    print(key, '- некорректные данные по зарплате!')
            except ValueError:
                print(key, '- некорректные данные по зарплате!')
except IOError:
    print('Ошибка ввода-вывода!')
finally:
    f.close()

print('Корректное кол-во зарплат сотрудников:', i)
print('Средняя зарплата сотрудников:', int(sum_salary / i))
