
# 6 p -------------------------------------------------

'''
Необходимо создать (не программно) текстовый файл,
где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество.
Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета
и общее количество занятий по нему. Вывести словарь на экран.
'''

end_dict = {}
try:
    with open('ДЗ 6 пункт.txt', 'r') as f:
        for my_str in f:
            my_li = my_str.split(':')
            my_dict = {my_li[0]: my_li[1]}
            my_str = my_li[1]
            for itm in my_str:
                if itm.isdigit() == False and itm != ' ':
                    my_str = my_str.replace(itm, ' ')
            my_li2 = list(map(int, my_str.split()))
            my_dict = {my_li[0]: sum(my_li2)}
            end_dict.update(my_dict)
except Exception:
    print('Ошибка ввода-вывода')

print(end_dict)
